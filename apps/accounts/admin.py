from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["full_name", "phone_number", "is_active"]
    list_filter = ["is_admin", "is_active"]
    readonly_fields = ["date_joined", "last_login"]
    fieldsets = [
        ("Personal info", {"fields": ["full_name", "phone_number", "password"]}),
        ("Permissions", {"fields": ["is_admin", "is_staff", "is_superuser"]}),
        ("Register & Login", {"fields": ["date_joined", "last_login"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["full_name", "phone_number", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["full_name", "phone_number"]
    ordering = ["-id"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
