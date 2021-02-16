from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import ticket, answer


class ticketserialaizer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     slug_field='username', read_only=True
    # )

    class Meta:
        model = ticket
        fields = ['user', 'id', 'subject', 'ticket_message',
                  'ps', 'status', 'category']
        extra_kwargs = {
            'status': {'read_only': True}
        }


class answerSerialaizer(serializers.ModelSerializer):
    ticket = serializers.SlugRelatedField(
         slug_field='subject', read_only=True)
    # user = serializers.SlugRelatedField(
    #     slug_field='username', read_only=True
    # )
    class Meta:
        model = answer
        fields = ['ticket', 'user', 'text', 'time']
