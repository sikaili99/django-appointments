from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import SimpleListFilter


# Register your models here.
@admin.register(User)
class addUser(UserAdmin):
    list_filter = ("role", )
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Role',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )
    ordering = ('email',)


