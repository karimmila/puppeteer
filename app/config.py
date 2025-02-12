from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    MAIL_USERNAME: str = "your_mailtrap_username"
    MAIL_PASSWORD: str = "your_mailtrap_password"
    MAIL_FROM: str = "noreply@example.com"
    MAIL_PORT: int = 2525
    MAIL_SERVER: str = "smtp.mailtrap.io"
    ENABLE_SMS: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
