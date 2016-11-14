# coding: utf-8

from django.db import models


class FeedBack(models.Model):
    class Meta:
        ordering = ('-created',)

    created = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    name = models.CharField(max_length=254)
    url = models.URLField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    message = models.TextField()

    def get_saved_data(self):
        return {
            'pk': self.pk,
            'created': self.created,
            'ip': self.ip,
            'name': self.name,
            'url': self.url,
            'email': self.email,
            'phone_number': self.phone_number,
            'message': self.message
        }
