# Generated by Django 4.2.6 on 2023-11-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0006_carservice_service_date_carservice_techinician_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parttoservice',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]