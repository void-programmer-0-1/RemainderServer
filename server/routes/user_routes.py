from fastapi import APIRouter, Depends, HTTPException, status
from schema.user_schema import CreateUserSchema, UpdateUserSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from database.database import get_session
from models.models import User

router = APIRouter(prefix="/user")


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserSchema, db: AsyncSession = Depends(get_session)):

    result = await db.execute(select(User).where(User.user_email == user.user_email))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User Already Exists")

    new_user = User(
        user_name=user.user_name,
        user_email=user.user_email,
        user_password=user.user_password
    )

    db.add(new_user)

    try:
        await db.commit()
        await db.refresh(new_user)

    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error {e}")

    return {"uid": new_user.uid, "message": "new user created successfully"}


@router.get("/get/{uid}")
async def get_user(uid: int, db: AsyncSession = Depends(get_session)):

    user = await db.execute(select(User).where(User.uid == uid))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    return user


@router.delete("/delete/{uid}")
async def delete_user(uid: int, db: AsyncSession = Depends(get_session)):

    user = await db.execute(select(User).where(User.uid == uid))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    await db.delete(user)

    try:
        await db.commit()

    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error {e}")

    return {"uid": user.uid, "message": "user has been deleted"}


@router.put("/update/{uid}")
async def update_user(uid: int, updated_user: UpdateUserSchema, db: AsyncSession = Depends(get_session)):

    user = await db.execute(select(User).where(User.uid == uid))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    # Check if the email already exists for another user
    email_result = await db.execute(select(User).where(
        User.user_email == updated_user.user_email, User.uid != uid)
    )
    existing_user = email_result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists.")

    user.user_name = updated_user.user_name
    user.user_email = updated_user.user_email
    user.user_password = updated_user.user_password

    user.touch()

    try:
        await db.commit()
        await db.refresh(user)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database Error during update.")

    return {"message": "User updated successfully", "user": user.to_dict()}