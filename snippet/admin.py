from django.contrib import admin

from .models import  Snippet, Language


admin.site.register(Snippet)
admin.site.register(Language)