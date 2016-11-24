from django.apps import AppConfig


class DjangoFeedbackApiConfig(AppConfig):
    name = 'django_feedback_api'
    verbose_name = 'FeedBacks'

    def ready(self):
        import django_feedback_api.signals.handlers
