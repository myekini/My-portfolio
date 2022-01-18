from django.contrib import admin
from . models import Name, Email, Message
# Register your models here.
admin.site.register(Name)
admin.site.register(Email)
admin.site.register(Message)
