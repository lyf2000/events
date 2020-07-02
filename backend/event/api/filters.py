from datetime import timedelta

from django.utils.timezone import localtime


def get_curr_time():
    return localtime()


def get_for_last_day():
    return get_curr_time() + timedelta(days=1)




def get_for_last_week():
    return get_curr_time() + timedelta(days=7)


def get_for_last_month():
    return get_curr_time() + timedelta(days=30)


PERIOD_CHOICES = {
    'day': get_for_last_day,
    'week': get_for_last_week,
    'month': get_for_last_month,
}
