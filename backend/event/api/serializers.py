from datetime import timedelta

from django.utils.timezone import localtime
from rest_framework import serializers

from event.models import Event
from event.tasks import remind_event
from users.api.serializers import OtherUserSerializer


def validate_only_after_hour(value):
    if value - localtime() <= timedelta(hours=1):
        raise serializers.ValidationError('You need to specify another time!')


class EventSerializer(serializers.ModelSerializer):
    author = OtherUserSerializer(required=False, read_only=True)
    created = serializers.DateTimeField(format="%b %Y", required=False)
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", validators=[validate_only_after_hour])

    class Meta:
        model = Event
        fields = ('id', 'author', 'title', 'text', 'date', 'created',
                  )

    # TODO PUT - update
    def update(self, instance, validated_data):
        date = validated_data.get('date', None)
        if date:
            if not date.strftime('%Y-%m-%d %H:%M') == instance.date.strftime('%Y-%m-%d %H:%M'):
                remind_event.apply_async((instance.id,), eta=date - timedelta(hours=1))
        return super(EventSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        user = self.context['request'].user
        event = Event.objects.create(
            **validated_data,
            author=user
        )
        remind_event.apply_async((event.id,), eta=event.date - timedelta(hours=1))
        return event
