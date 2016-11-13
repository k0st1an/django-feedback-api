# coding: utf-8

from rest_framework import serializers

from django_feedback_api.models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ('created', 'ip', 'name', 'url', 'email', 'mobile_number')
        read_only_fields = ('pk',)