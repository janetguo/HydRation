from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/hydration_db"
    SECRET_KEY: str = "dev_secret_key"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings() 