import os
import redis

class Config:
    GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS", "false") == "true"

    if GITHUB_ACTIONS:
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        REDIS_HOST = "localhost"
    else:
        DB_USER = os.getenv("DB_USER")
        DB_PASS = os.getenv("DB_PASS")
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")

        SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
        REDIS_HOST = os.getenv("REDIS_HOST")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default-key")

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = False

# Redis bağlantısı
redis_client = redis.Redis(
    host=Config.REDIS_HOST,
    port=6379,
    db=0
)
