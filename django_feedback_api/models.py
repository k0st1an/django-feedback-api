# coding: utf-8

from django.db import models


class FeedBack(models.Model):
    class Meta:
        ordering = ('-created',)

    created = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    name = models.CharField(max_length=254)
    url = models.URLField()
    form_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    message = models.TextField(blank=True)

    def get_saved_data(self):
        return {
            'pk': self.pk,
            'created': self.created,
            'ip': self.ip,
            'name': self.name,
            'url': self.url,
            'form_name': self.form_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'message': self.message
        }
