from datetime import timedelta
from time import sleep

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import localtime


from event.models import Event


@shared_task
def remind_event(id):
    try:
        print('id', id)
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return False
    print('check')
    if not check_to_remind_event(event):
        return False

    mail_subject = 'MEETIIIING AAAAA.'
    context = {
        'username': event.author.username,
        'meet_date': event.date.strftime('%Y-%m-%d %H:%M'),
        'title': event.title,
        'text': event.text
    }
    send_message('event/meeting_remind.html', context, mail_subject, event.author.email)


def send_message(template_name, message_context, mail_subject, to_email):
    message = render_to_string(template_name, message_context)
    msg = EmailMultiAlternatives(mail_subject, '', '', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()


def check_to_remind_event(event):
    now = localtime() + timedelta(hours=1)
    left = event.date - timedelta(minutes=1)
    right = event.date + timedelta(minutes=1)
    if now >= left and now < right:
        return True
    return False
