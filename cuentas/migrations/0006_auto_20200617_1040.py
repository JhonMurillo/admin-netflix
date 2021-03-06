# Generated by Django 3.0.7 on 2020-06-17 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('cuentas', '0005_auto_20200617_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
