# Generated by Django 5.0 on 2023-12-28 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_menuitem_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='slug',
        ),
    ]