from django.contrib import admin
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import User


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user',)
    search_fields = ('user__username', 'user__email', 'user__first_name' 'user__last_name')
    list_filter = ('created', 'updated', 'user__is_active', 'user__is_staff')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                'biography',
            ),
        }),
        ('metadata', {
            'fields': (('created', 'updated'),),
        }),
    )

    readonly_fields = ('created', 'updated')


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
