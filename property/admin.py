from django.contrib import admin
from django.db import models
from .models import Flat, Complaint



    
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]
    list_display = ("address", "price", "new_building", "construction_year", "town")
    list_editable = ["new_building"]
    list_filter = ["new_building"]

admin.site.register(Flat, AuthorAdmin)

@admin.register(Complaint)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat")

