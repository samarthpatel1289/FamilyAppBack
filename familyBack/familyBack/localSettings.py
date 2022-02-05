# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'familyapp',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'POST': '',
    }
}