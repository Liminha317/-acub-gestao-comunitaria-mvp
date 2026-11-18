from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "chave-de-teste-automatizado-acub"
DEBUG = False
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "core",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
