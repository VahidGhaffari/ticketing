from rest_framework import serializers, status, viewsets
from .models import ticket, answer
from .serialaizers import ticketserialaizer, answerSerialaizer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class ticketViewset(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticketserialaizer

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
