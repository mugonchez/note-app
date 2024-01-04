from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'owner']


admin.site.register(Note, NoteAdmin)
