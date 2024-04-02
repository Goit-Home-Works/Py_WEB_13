import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_PATH = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_PATH.joinpath(".env"))
APP_ENV = os.getenv("APP_ENV")
print(f"{APP_ENV=}")


class Settings(BaseSettings):
    app_mode: str = "prod"
    app_name: str = "contacts"
    app_host: str = "0.0.0.0"
    app_port: int = 9000
    sqlalchemy_database_url: str = os.getenv(
        "DATABASE_URL"
    ) 
    # Assuming DATABASE_URL is set in your .env file
    token_secret_key: str = os.getenv("TOKEN_SECRET_KEY", "some_SuPeR_key")
    token_algorithm: str = os.getenv("TOKEN_ALGORITHM", "HS256")
    mail_username: str = os.getenv("MAIL_USERNAME", "user@example.com")
    mail_password: str = os.getenv("MAIL_PASSWORD", "")
    mail_from: str = os.getenv("MAIL_FROM", "user@example.com")
    mail_port: int = int(os.getenv("MAIL_PORT", 465))
    mail_server: str = os.getenv("MAIL_SERVER", "")
    mail_from_name: str = os.getenv("MAIL_FROM_NAME", "")
    redis_host: str = os.getenv("REDIS_HOST", "localhost")
    redis_port: int = int(os.getenv("REDIS_PORT", 6379))
    cloudinary_name: str = os.getenv("CLOUDINARY_NAME", "some_name")
    cloudinary_api_key: str = os.getenv("CLOUDINARY_API_KEY", "0000000000000")
    cloudinary_api_secret: str = os.getenv("CLOUDINARY_API_SECRET", "some_secret")
    rate_limiter_times: int = int(os.getenv("RATE_LIMITER_TIMES", 2))
    rate_limiter_seconds: int = int(os.getenv("RATE_LIMITER_SECONDS", 5))
    sendgrid_api_key: str = os.getenv(("SENDGRID_API_KEY=", "some_pass"))

    class Config:
        extra = "ignore"
        env_file = (
            str(BASE_PATH.joinpath(f".env-{APP_ENV}"))
            if APP_ENV
            else str(BASE_PATH.joinpath(".env"))
        )
        env_file_encoding = "utf-8"
        print(f"{env_file=}")


settings = Settings()

if __name__ == "__main__":
    print(f"{BASE_PATH =}")
    print(f"{settings.Config.env_file=}")
    print(f"{settings=}")
