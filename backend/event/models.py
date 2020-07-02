from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy


class Event(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='events', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=750)
    date = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)

    ordering = ['-date']

    def __str__(self):
        return f'Meet({self.id})'

    def get_normal_time(self):
        return self.date.strftime('%Y-%m-%d %H:%M')
