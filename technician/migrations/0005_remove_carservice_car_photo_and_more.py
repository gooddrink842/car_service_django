# Generated by Django 4.2.6 on 2023-11-02 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0004_carservice_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carservice',
            name='car_photo',
        ),
        migrations.RemoveField(
            model_name='carservice',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='carservice',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='carservice',
            name='parts_to_service',
        ),
        migrations.CreateModel(
            name='PartToService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_to_service', models.TextField()),
                ('car_photo', models.ImageField(blank=True, null=True, upload_to='car_photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('car_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_to_service', to='technician.carservice')),
            ],
        ),
    ]
