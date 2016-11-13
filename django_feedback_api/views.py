# coding: utf-8

from rest_framework.viewsets import ModelViewSet

from django_feedback_api.models import FeedBack
from django_feedback_api.serializers import FeedBackSerializer


class FeedBackCreateViewSet(ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    http_method_names = ['post', 'options']
