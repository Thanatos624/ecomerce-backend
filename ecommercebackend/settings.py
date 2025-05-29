from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # <-- This is the one you're missing
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'users',
    'products',
    'orders',
]
ROOT_URLCONF = 'ecommercebackend.urls'
AUTH_USER_MODEL = 'users.CustomUser'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
SECRET_KEY = 'abc123xyz!$#somethingverysecret987654'
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # REQUIRED
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # REQUIRED
    'django.contrib.messages.middleware.MessageMiddleware',  # REQUIRED
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can set this to point to custom template dirs if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecomdb',            # Your PostgreSQL database name
        'USER': 'postgres',          # Your PostgreSQL username
        'PASSWORD':'2003',    # Your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Optional: use if you have a 'static/' folder in root
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Optional: for `collectstatic` in production




