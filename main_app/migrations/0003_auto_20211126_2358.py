# Generated by Django 3.2.9 on 2021-11-26 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
    ]