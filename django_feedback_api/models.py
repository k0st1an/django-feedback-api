# coding: utf-8

from django.db import models


class FeedBack(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    name = models.CharField(max_length=254)
    url = models.URLField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15, blank=True)
