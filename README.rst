Django FeedBack JSON
====================

Set up
------

`settings.py`::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'django_feedback_api',
    ]

`urls.py`::

    urlpatterns = [
        ...
        url(r'^api/', include('django_feedback_api.urls')),
    ]

