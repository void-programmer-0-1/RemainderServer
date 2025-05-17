from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):

    database_url: str
    app_name: str = "Remainder App"
    app_version: str = "0.1.0"
    app_description: str = "Events and Task remainder server for you"

    class Config:
        env_file = ".env"


app_settings = AppSettings()
