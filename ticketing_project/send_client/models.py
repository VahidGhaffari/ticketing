from os import times
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User


class ticket(models.Model):
    STATUS_CHOISES = (
        ('unrd', 'Unread'),
        ('rd', 'read '),
        ('answd', 'has been answered'),
        ('termid', 'Terminated')
    )
    subject = models.CharField(max_length=50)
    ticket_message = models.CharField(max_length=256)
    status = models.CharField(
        max_length=6, choices=STATUS_CHOISES)
    ps = models.FileField(blank=True)

    def __str__(self):
        return self.subject


class answer(models.Model):
    u = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=512)
    admin = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
    t = models.ForeignKey(ticket, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.text