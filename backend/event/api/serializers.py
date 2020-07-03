import datetime
from datetime import timedelta
from event.tasks import remind_event
from rest_framework import serializers
from django.utils.timezone import localtime
from event.models import Event
from users.api.serializers import OtherUserSerializer


def validate_only_after_hour(value):
    if value - localtime() <= timedelta(hours=1):
        raise serializers.ValidationError('You need to specify another time!')


class  EventSerializer(serializers.ModelSerializer):
    author = OtherUserSerializer(required=False, read_only=True)
    created = serializers.DateTimeField(format="%b %Y", required=False)
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", validators=[validate_only_after_hour])

    # marked = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Event
        fields = ('id', 'author', 'title', 'text', 'date', 'created',
                  # , 'marked'
                  )

    # def get_marked(self, obj):
    #     if self.context['request'].user in obj.added.all():
    #         return 'true'
    #     return 'false'
    # TODO через час и более только
    def create(self, validated_data):
        user = self.context['request'].user
        event = Event.objects.create(
            **validated_data,
            author=user
        )
        remind_event.apply_async((event.id,), eta=event.date - timedelta(hours=1))
        return event
