from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from blog_vai.accounts.models import SiteUser


UserModel = get_user_model()


@admin.register(UserModel)
class SiteUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
