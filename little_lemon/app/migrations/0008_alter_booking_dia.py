# Generated by Django 5.0 on 2023-12-29 01:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_booking_dia_booking_seats_alter_booking_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dia',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 1, 31, 28, 312748, tzinfo=datetime.timezone.utc)),
        ),
    ]
