from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    mongodb_url: str
    jwt_secret: str
    jwt_algorithm: str
    jwt_expires: int
    model_config = SettingsConfigDict(env_file=".env")
