from django.contrib import admin

from .models import *

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'displayname', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('user__id', 'user__username', 'displayname')


admin.site.register(Profile, AccountAdmin)
