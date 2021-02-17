from os import times
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ticket(models.Model):

    STATUS_CHOISES = (
        ('1', 'Unread'),
        ('2', 'read '),
        ('3', 'has been answered'),
        ('4', 'Terminated')
    )
    subject = models.CharField(max_length=50)
    ticket_message = models.TextField()
    status = models.CharField(
        max_length=6, choices=STATUS_CHOISES, default='1', null=True)
    ps = models.FileField(blank=True, upload_to="protect/",
                          validators=[FileExtensionValidator()])
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class answer(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, null=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.text
