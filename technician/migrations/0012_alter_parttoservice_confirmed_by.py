# Generated by Django 4.2.6 on 2023-11-22 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('technician', '0011_parttoservice_confirmed_by_parttoservice_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parttoservice',
            name='confirmed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
