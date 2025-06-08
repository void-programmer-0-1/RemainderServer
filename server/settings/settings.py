from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):

    database_url: str
    app_name: str = "Remainder App"
    app_version: str = "0.1.0"
    app_description: str = "Events and Task remainder server for you"
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expiry_time: str
    jwt_refresh_token_expiry_time: str
    host: str
    port: str
    threads: int
    workers: int
    worker_class: str

    class Config:
        env_file = ".env"


app_settings = AppSettings()

