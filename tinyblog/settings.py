"""
Django settings for tinyblog project.

Generated by 'django-admin startproject' using Django 1.11.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$17wgy2ahj60ur-=n8azr71-159r2&-j$eq$vwmzff@ozvr7&('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs',
    'comments',
    'haystack',
    'users',
    'crispy_forms',


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

ROOT_URLCONF = 'tinyblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'tinyblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


HAYSTACK_CONNECTIONS={
    'default':{
        #django haystack 使用的搜索引擎
        'ENGINE':'blogs.whoosh_cn_backend.WhooshEngine',
        # 索引文件存放的目录(使用搜索引擎需要建立索引文件)
        'PATH':os.path.join(BASE_DIR,'templates/whoosh_index')
    }
}

# 每2项结果为1页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 2
# 多久更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# 重写了AbstractUser类,需要加上这句支持重写
AUTH_USER_MODEL = 'users.User'


# 设置登录和注销跳转的URL,硬编码
# LOGIN_REDIRECT_URL = '/index/'
LOGOUT_REDIRECT_URL = '/index/'

STATIC_URL = '/static/'


# 媒体文件上传的路径是工程目录下的media文件夹---文件夹自己创建
# 用户上传,如post的image,upload_to是avator,会在MEDIA_ROOT下,自动创建目录
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'

# django在开发环境提供的方便的Backends,模拟真实邮件的发送.
# 直接发送邮件到终端
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#  点击忘记密码后,会依次进入users/password_reset/  这个页面要求输入用户邮箱
#  邮箱输入完毕后,会跳到这个页面users/password_reset/done/,告知密码已发送,要求去链接访问
#  在后台(终端)收到邮件,把链接copy到浏览器   http://127.0.0.1:8000/users/reset/MTU/4vh-7b36e2fe2b754eeca189/
#  到浏览器后跳转到users/reset/MTU/set-password/  输入新密码,确认密码
#  密码设置成功后,又跳转到 /users/reset/done/ 告知密码设置成功