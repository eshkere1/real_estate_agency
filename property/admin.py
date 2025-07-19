from django.contrib import admin
from django.db import models
from .models import Flat


    
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]


admin.site.register(Flat, AuthorAdmin)
