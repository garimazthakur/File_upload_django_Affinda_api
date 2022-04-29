from django.contrib import admin

# Register your models here.

from .models import Snippet, Affinda

class SnippetAdmin(admin.ModelAdmin):
    randomly_fileds=('highlighted',)



admin.site.register(Snippet)
admin.site.register(Affinda)