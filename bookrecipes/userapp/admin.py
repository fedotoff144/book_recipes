from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'email', 'is_superuser', 'is_active', 'gender']
    ordering = ['pk']
    list_display_links = 'username', 'email'
    search_fields = 'username', 'first_name'
    search_help_text = 'Поиск по полю username и first_name'

# admin.site.register(User, UserAdmin)
