from django.contrib import admin
from . models import Ticket, answer, Category


admin.site.register(Ticket)
admin.site.register(answer)
admin.site.register(Category)
