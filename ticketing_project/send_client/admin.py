from django.contrib import admin
from . models import ticket, answer, Category


admin.site.register(ticket)
admin.site.register(answer)
admin.site.register(Category)
