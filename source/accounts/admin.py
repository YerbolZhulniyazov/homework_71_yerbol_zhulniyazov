from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'user_info', 'phone', 'gender')
    list_filter = ('email', 'avatar', 'user_info', 'phone', 'gender')
    search_fields = ('email', 'avatar', 'phone', 'gender')
    fields = ('email', 'avatar', 'user_info', 'phone', 'gender')
    readonly_fields = ('id',)


admin.site.register(Account, AccountAdmin)