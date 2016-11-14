Django FeedBack API
===================

Requirements
------------

- django
- django rest framework


Set up
------

Simple `settings.py`::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'django_feedback_api',
    ]
    EMAIL_HOST = 'smtp.yandex.ru'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_TIMEOUT = 5
    EMAIL_HOST_USER = 'email@example.com'
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    SERVER_EMAIL = 'email@example.com'
    EMAIL_HOST_PASSWORD = 'PASSWORD'
    MANAGERS = [('Ivanov Ivan', 'email2@example.com')]
    # Optional
    FEEDBACK_SUBJECT = 'Django FeedBack: New feedback'

`urls.py`::

    urlpatterns = [
        ...
        url(r'^api/', include('django_feedback_api.urls')),
    ]

Sent POST to ``http://your.site/api/feedback/``.
