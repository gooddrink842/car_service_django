# Generated by Django 4.2.6 on 2023-11-22 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('technician', '0010_carservice_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='parttoservice',
            name='confirmed_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='confirmed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='parttoservice',
            name='reason',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='parttoservice',
            name='parts_to_service',
            field=models.TextField(default=None),
        ),
    ]