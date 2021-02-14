from django.contrib.auth.models import User
from rest_framework import serializers, status, viewsets
from rest_framework.settings import api_settings

from .models import ticket, answer
from .serialaizers import ticketserialaizer, answerSerialaizer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User


class ticketViewset(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticketserialaizer

    # def create(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         ticket_data = request.data
    #         new_ticket = ticket.objects.create(
    #             user=User.id, subject=ticket_data["subject"], ticket_message=ticket_data[
    #                 "ticket_message"], status=ticket_data["status"],
    #             ps=ticket_data["ps"], category=ticket_data["category"])
    #
    #         new_ticket.save()
    #         serializer = ticketserialaizer(new_ticket)
    #         return Response(serializer.data, many=True)
    #         new_ticket.save()

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
        print(type(answer_data))
        print(answer_data)
        answer_data["user"] = current_user.id
        print(answer_data)
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
