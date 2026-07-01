import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aimastertoolmax',
        'USER': 'root',
        'PASSWORD': 'qingwen123',
        'HOST': 'ai-mysql',
        'PORT': '3306',
	    'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://ai-redis:6379/1",  # 根据您的 Redis 配置更改
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

OPENAI_SERVER = "http://43.134.24.122:8000"