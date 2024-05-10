from pathlib import Path

from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'sdf45r24fsf2tra6il9reev!36(qkqdf*17y@h+*@zz_p!=$n94yoyn4&gbv8+o'

INTERNAL_IPS = [
    '127.0.0.1'
]

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'channels',
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'embed_video',
    'debug_toolbar',
    'redisboard',
    'rest_framework',
    'froala_editor',

    'courses.apps.CoursesConfig',
    'students.apps.StudentsConfig',
    'chat.apps.ChatConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'education_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': []
        ,
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

WSGI_APPLICATION = 'education_platform.wsgi.application'
ASGI_APPLICATION = "education_platform.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)]
        },
    },
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = reverse_lazy('student_course_list')

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379'
        # 'LOCATION': 'redis://redis:6379',
    }
}

CACHE_MIDDLEWARE_SECONDS = 10
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_KEY_PREFIX = 'educa'

# DRF

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
# Froala

FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier', 'code_view', 'colors', 'draggable', 'emoticons',
                         'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image',
                         'inline_style',
                         'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert',
                         'quote', 'save', 'table',
                         'url', 'video')

if DEBUG:
    from education_platform.conf.local import *
else:
    from education_platform.conf.prod import *
