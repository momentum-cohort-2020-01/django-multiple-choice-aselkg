from django.contrib import admin
from .models import Snippet, Lang

admin.site.register(Snippet)
admin.site.register(Lang)