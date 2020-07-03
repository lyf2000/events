from event.models import Event
from django.utils.timezone import localtime
from datetime import timedelta
from event.tasks import remind_event
e = Event.objects.first()

e.date = localtime() + timedelta(hours=1, minutes=1)
e.save()


remind_event.apply_async((e.id,), eta=e.date - timedelta(hours=1))