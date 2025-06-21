class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@host.docker.internal/large-blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "gizli-bir-key"

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"  # Çok önemli! Cross-origin çağrılarda "None" da olabilir
    SESSION_COOKIE_SECURE = False  # Sadece HTTPS'te True olmalı
