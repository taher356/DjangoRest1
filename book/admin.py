from django.contrib import admin
from . import models


class AdminModel(admin.ModelAdmin):
    list_display = ['name', 'fav', 'created_at']


admin.site.register(models.Book, AdminModel)
