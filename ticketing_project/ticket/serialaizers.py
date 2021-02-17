from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Ticket, answer


class ticketserialaizer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     slug_field='username', read_only=True
    # )

    class Meta:
        model = Ticket
        fields = ['subject', 'ticket_message',
                  'ps', 'status', 'category', 'created_at']
        extra_kwargs = {
            'status': {'read_only': True}
        }


class answerSerialaizer(serializers.ModelSerializer):
    # ticket = serializers.SlugRelatedField(
    #     slug_field='subject', read_only=True)
    # user = serializers.SlugRelatedField(
    #     slug_field='username', read_only=True
    # )

    class Meta:
        model = answer
        fields = ['ticket', 'text', 'created_at']
