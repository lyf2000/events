from rest_framework import serializers

from ..models import User


class OtherUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
        read_only_fields = ['username']
