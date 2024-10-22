# Generated by Django 5.0.1 on 2024-10-22 13:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(null=True),
        ),
    ]