import datetime
from time import sleep

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.db.models import Case, When, Q, Value, IntegerField, BooleanField
from django.template.loader import render_to_string
from django.utils import timezone

from event.api.filters import get_curr_time
from event.models import Event


@shared_task
def remind_event(id, datetime):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return
    if not datetime == event.date.strftime('%Y-%m-%d %H:%M'):
        return
    mail_subject = 'MEETIIIING AAAAA.'
    context = {
        'username': event.author.username,
        'meet_date': event.date.strftime('%d/%m/%Y %H:%M'),
        'title': event.title
    }
    # send_message.delay('event/meeting_remind.html', context, mail_subject, event.author.email)
    send_message('event/meeting_remind.html', context, mail_subject, event.author.email)


@shared_task
def send_message(template_name, message_context, mail_subject, to_email):
    message = render_to_string(template_name, message_context)
    msg = EmailMultiAlternatives(mail_subject, '', '', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()
    print('remind_meets send_message to', to_email)


@shared_task
def check_to_remind_meets():
    meets_to_be_reminded = Event.objects.annotate(in_hour=Case(
    When(Q(date__gte=get_curr_time())
         & Q(date__lte=timezone.now() + datetime.timedelta(hours=1)),
         then=Value(True)),
    default=Value(False),
    output_field=BooleanField())).filter(in_hour=True)
    print(meets_to_be_reminded)

@shared_task
def a():
    sleep(2)
    return 1
