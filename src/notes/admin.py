from django.contrib import admin
from .models import Category, Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'completed')
    list_display_links = ('title', 'category')
    search_fields = ('id', 'title')
    list_editable = ('completed',)
    list_filter = ('completed',)


admin.site.register(Category)
admin.site.register(Note, NoteAdmin)
