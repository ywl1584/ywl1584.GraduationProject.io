# Generated by Django 2.1.2 on 2019-01-23 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]