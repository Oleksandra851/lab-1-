"""
Налаштування Django для проєкту mysite.

Згенеровано командою 'django-admin startproject' за допомогою Django 5.2.7.

Для отримання додаткової інформації про цей файл див.
https://docs.djangoproject.com/en/5.2/topics/settings/

Повний список налаштувань та їх значень див.
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Створіть шляхи всередині проєкту ось так: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Налаштування швидкого старту розробки – непридатні для продакшену
# див. https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: тримайте секретний ключ, який використовується у виробництві, у таємниці!
SECRET_KEY = 'django-insecure-r_j67dgjfzhwty0r7m$7ddid!_k_o*28kcnj0q8&*9ds8p3g=-'

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: не запускайте з увімкненим налагодженням у продакшені!
DEBUG = True

ALLOWED_HOSTS = []

# Визначення програми

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# База даних
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres_pass',
    }
}

# Перевірка пароля
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Інтернаціоналізація
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Статичні файли (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Тип поля первинного ключа за замовчуванням
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
