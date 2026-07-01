import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aimastertoolmax',
        'USER': os.environ.get('dbuser'),
        'PASSWORD': os.environ.get('dbpassword'),
        'HOST': '127.0.0.1',
        'PORT': '3306',
	    'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",  # 根据您的 Redis 配置更改
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# OPENAI_SERVER = "http://127.0.0.1:8001"
OPENAI_SERVER = "http://43.134.24.122:8000"