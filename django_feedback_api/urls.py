# coding: utf-8

from rest_framework import routers

from django_feedback_api.views import FeedBackCreateViewSet

router = routers.SimpleRouter()
router.register(r'feedback', FeedBackCreateViewSet)

urlpatterns = router.urls
