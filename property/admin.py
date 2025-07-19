from django.contrib import admin
from django.db import models
from .models import Flat


    
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]


admin.site.register(Flat, AuthorAdmin)
