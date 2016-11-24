# coding: utf-8

from django.contrib import admin

from django_feedback_api.models import FeedBack


class FeedBackAdmin(admin.ModelAdmin):
    
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['ip', 'name', 'form_name', 'email', 'phone_number']
    list_per_page = 30
    list_display = ('name', 'email', 'phone_number')

    readonly_fields = ('created',)


admin.site.register(FeedBack, FeedBackAdmin)
