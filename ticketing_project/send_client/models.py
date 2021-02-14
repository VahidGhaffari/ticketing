from os import times
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class ticket(models.Model):
    STATUS_CHOISES = (
        ('unrd', 'Unread'),
        ('rd', 'read '),
        ('answd', 'has been answered'),
        ('termid', 'Terminated')
    )
    #owner = models.CharField(max_length=100, primary_key=True)
    subject = models.CharField(max_length=50)
    ticket_message = models.TextField()
    status = models.CharField(
        max_length=6, choices=STATUS_CHOISES, default='unrd', null=True)
    ps = models.FileField(blank=True)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.subject


class answer(models.Model):
    ticket = models.ForeignKey(ticket, on_delete=models.CASCADE, null=False)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, null=False)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
