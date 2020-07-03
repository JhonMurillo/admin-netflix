from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+')
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Provider(BaseModel):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20,  default=None, blank=True, null=True)
    email = models.EmailField(max_length=200,  default=None, blank=True, null=True)
    def __str__(self):
        return 'Proveedor: {}'.format(self.name)
class Account(BaseModel):
    provider = models.ForeignKey(Provider,on_delete=models.CASCADE,  default=None, blank=True, null=True, related_name='+')
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return 'Cuenta: {}, Password: XXXXXX{}'.format(self.email, self.password)
        
class AccountDetail(BaseModel):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    pay_value = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    active_at = models.DateField()
    expire_at = models.DateField()
    def __str__(self):
        return 'Cuenta: {}, Password: XXXXXX{}, Activado el: {}'.format(self.account.email, self.account.password, self.active_at)


class Profile(BaseModel):
    account = models.ForeignKey(Account,on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE,  default=None, blank=True, null=True, related_name='+')
    profile = models.ForeignKey('users.Profile',on_delete=models.CASCADE,  default=None, blank=True, null=True, related_name='+')
    client_name = models.CharField(max_length=200)
    profile_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, default=None, blank=True, null=True)
    email = models.EmailField(max_length=200,default=None, blank=True, null=True)
    pin = models.CharField(max_length=4)
    pay_value = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    def __str__(self):
        return 'Cuenta: {}, Perfil: {}'.format(self.account.email, self.profile_name)


class ProfileDetail(BaseModel):
    CURRENT='CURRENT'
    RENOVATED='RENOVATED'
    CANCELED='CANCELED'
    STATUSES = (
      (CURRENT, 'Actual'),
      (RENOVATED, 'Renovado'),
      (CANCELED, 'Cancelado')
      )

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    is_pay = models.BooleanField(default=False)
    pay_value = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    active_at = models.DateField()
    expire_at = models.DateField()
    status_detail = models.CharField(max_length=20, choices=STATUSES, default=CURRENT)
    def __str__(self):
        return 'Cuenta: {}, Password: XXXXXX{}, Perfil: {}, Activado el: {}'.format(self.profile.account.email, self.profile.account.password, self.profile.profile_name, self.active_at)


class Withdraw(BaseModel):
    description = models.TextField(max_length=4000)
    withdraw_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    def __str__(self):
        return 'Descripcion: {}, Pago: {}'.format(self.description, self.withdraw_value)


class Wallet(BaseModel):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    description = models.TextField(max_length=4000)
    wallet_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    def __str__(self):
        return 'Descripcion: {}, Pago: {}'.format(self.description, self.wallet_value)
