import os
from django.contrib.auth.models import User
from django.urls.conf import path
from rest_framework import serializers, status, viewsets
from rest_framework.settings import api_settings

from .models import Ticket, answer
from .serialaizers import ticketserialaizer, answerSerialaizer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.http import FileResponse
from django.contrib.auth.decorators import login_required


class ticketViewset(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = ticketserialaizer

    def create(self, request, *args, **kwargs):
        ticket_data = request.data
        current_user = request.user
        print(type(ticket_data))
        print(ticket_data)
        ticket_data["user"] = current_user.id
        print(ticket_data)
        serializer = self.get_serializer(data=ticket_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser(), ]
        if self.action == 'create':
            return [IsAuthenticated(), ]
        if self.action == 'retrieve':
            return [IsAdminUser(), ]
        if self.action == 'update':
            return [IsAdminUser(), ]
        if self.action == 'partial_update':
            return [IsAdminUser(), ]
        if self.action == 'destroy':
            return [IsAdminUser(), ]
        return super(ticketViewset, self).get_permissions()


class answerticketViewset(viewsets.ModelViewSet):
    queryset = answer.objects.all()
    serializer_class = answerSerialaizer

    def create(self, request, *args, **kwargs):
        answer_data = request.data
        current_user = request.user
        answer_data["user"] = current_user.id
        serializer = self.get_serializer(data=answer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser(), ]
        if self.action == 'create':
            return [IsAuthenticated(), ]
        if self.action == 'retrieve':
            return [IsAdminUser(), ]
        if self.action == 'update':
            return [IsAdminUser(), ]
        if self.action == 'partial_update':
            return [IsAdminUser(), ]
        if self.action == 'destroy':
            return [IsAdminUser(), ]
        return super(answerticketViewset, self).get_permissions()
