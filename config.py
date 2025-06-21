import os

class Config:
    if os.environ.get("GITHUB_ACTIONS") == "true":
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # CI/CD ortamı için
    else:
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@host.docker.internal/large-blog"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "gizli-bir-key"

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = False
