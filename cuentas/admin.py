from django.contrib import admin

# Register your models here.
from cuentas.models import Account, AccountDetail, Profile, ProfileDetail, Provider, Withdraw, Wallet



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

class AccountDetailInline(admin.TabularInline):
    model = AccountDetail
    extra = 1
    can_delete = False
    verbose_name_plural = 'Detalle De La Cuenta'

class AccountAdmin(admin.ModelAdmin):
    inlines = (AccountDetailInline,)

admin.site.register(Account, AccountAdmin)

admin.site.register(AccountDetail, AccountDetailAdmin)

class ProfileDetailAdmin(admin.ModelAdmin):
    list_display = ('pk','profile_client_name','profile_name','account_email','pin','profile_pay_value','pay_value','is_pay','status_detail', 'active_at', 'expire_at')
    list_display_links = ('pk','profile_client_name', 'account_email')
    list_editable = ('is_pay','pay_value', 'status_detail')
    search_fields = (
        'profile__account__email',
        'profile__client_name',
        'is_pay',
        'status_detail',
        'active_at',
        'expire_at'
    )

    list_filter=(
        'profile__account__email',
        'profile__client_name',
        'status_detail',
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

class ProfileDetailInline(admin.TabularInline):
    model = ProfileDetail
    extra = 1
    can_delete = False
    verbose_name_plural = 'Detalle Del Perfil'

class WalletInline(admin.TabularInline):
    model = Wallet
    extra = 0
    max_num=0
    can_delete = False
    verbose_name_plural = 'Detalle Del Perfil'

class ProfileAdmin(admin.ModelAdmin):
    inlines = (ProfileDetailInline, WalletInline)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(ProfileDetail, ProfileDetailAdmin)

admin.site.register(Provider)

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('pk','description','withdraw_value')
    list_display_links = ('pk','description')
    list_editable = ('withdraw_value',)
    search_fields = (
        'description',
        'withdraw_value',
        'created_at'
    )

    list_filter=(
        'description',
        'withdraw_value',
        'created_at'
    )

    ordering = ('-created_at',)

admin.site.register(Withdraw, WithdrawAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('pk','profile_client_name','profile_name','description','wallet_value')
    list_display_links = ('pk','profile_client_name','profile_name','description')
    list_editable = ('wallet_value',)
    search_fields = (
        'profile__client_name',
        'profile__name',
        'description',
        'wallet_value',
        'created_at'
    )

    list_filter=(
        'profile__client_name',
        'profile__profile_name',
        'description',
        'wallet_value',
        'created_at'
    )

    ordering = ('-created_at',)

    def profile_client_name(self, obj):
        return obj.profile.client_name
    def profile_name(self, obj):
        return obj.profile.profile_name

admin.site.register(Wallet, WalletAdmin)