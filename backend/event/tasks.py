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
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        print('!!expired!!')
        return False
    print('OK')
    if not check_to_remind_event(event):
        return False

    mail_subject = 'MEETIIIING AAAAA.'
    context = {
        'username': event.author.username,
        'meet_date': event.date.strftime('%Y-%m-%d %H:%M'),
        'title': event.title
    }
    print(send_message('event/meeting_remind.html', context, mail_subject, event.author.email))


def send_message(template_name, message_context, mail_subject, to_email):
    message = render_to_string(template_name, message_context)
    msg = EmailMultiAlternatives(mail_subject, '', '', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()


def check_to_remind_event(event):
    now = localtime() + timedelta(hours=1)
    left = event.date - timedelta(minutes=1)
    right = event.date + timedelta(minutes=1)
    print(now, left, right)
    if now >= left and now < right:
        return True
    return False


@shared_task
def a():
    sleep(2)
    return 1
