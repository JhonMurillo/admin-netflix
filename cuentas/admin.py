from django.contrib import admin

# Register your models here.
from cuentas.models import Account, AccountDetail, Profile, ProfileDetail

admin.site.register(Account)

class AccountDetailAdmin(admin.ModelAdmin):
    list_display = ('pk','account_email', 'pay_value', 'active_at', 'expire_at')
    list_display_links = ('pk', 'account_email')
    list_editable = ('pay_value',)
    search_fields = (
        'account__email',
    )

    list_filter=(
        'account__email',
        'active_at',
        'expire_at'
    )

    ordering = ('account__email', 'active_at', 'pk', 'created_at')

    def account_email(self, obj):
        return obj.account.email

admin.site.register(AccountDetail, AccountDetailAdmin)

admin.site.register(Profile)

class ProfileDetailAdmin(admin.ModelAdmin):
    list_display = ('pk','profile_client_name','profile_name','account_email','pin','profile_pay_value','pay_value','is_pay', 'active_at', 'expire_at')
    list_display_links = ('pk','profile_client_name', 'account_email')
    list_editable = ('is_pay','pay_value')
    search_fields = (
        'profile__account__email',
        'profile__client_name',
        'is_pay',
        'active_at',
        'expire_at'
    )

    list_filter=(
        'profile__account__email',
        'profile__client_name',
        'active_at',
        'expire_at'
    )

    ordering = ('profile__account__email', 'active_at', 'pk')

    def account_email(self, obj):
        return obj.profile.account.email
    def profile_client_name(self, obj):
        return obj.profile.client_name
    def profile_name(self, obj):
        return obj.profile.profile_name
    def profile_phone(self, obj):
        return obj.profile.phone
    def profile_email(self, obj):
        return obj.profile.email
    def pin(self, obj):
        return obj.profile.pin
    def profile_pay_value(self, obj):
        return obj.profile.pay_value

admin.site.register(ProfileDetail, ProfileDetailAdmin)

