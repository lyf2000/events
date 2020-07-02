import datetime
import os

from django import forms
from django.contrib import admin

# Register your models here.


# from django.contrib.gis.db import models
# from mapwidgets.widgets import GooglePointFieldWidget


# class CityAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.PointField: {"widget": GooglePointFieldWidget}
#     }
from django.db.models import Count


from django.utils.safestring import mark_safe
from django.db import models

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
