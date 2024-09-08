from django.contrib import admin

from users.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active', 'first_name', 'last_name')
    list_filter = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email')
