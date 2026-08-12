import os

# Cập nhật TEMPLATES DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/static')
        ],
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

# Thêm STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/static')
]

# Cập nhật ALLOWED_HOSTS và CSRF_TRUSTED_ORIGINS
ALLOWED_HOSTS = ['localhost', 'your-app-url-here']
CSRF_TRUSTED_ORIGINS = ['https://your-app-url-here']