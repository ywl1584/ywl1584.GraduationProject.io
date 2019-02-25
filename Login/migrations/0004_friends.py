# Generated by Django 2.1.2 on 2019-01-23 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_remove_user_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(blank=True, related_name='my_friends', to='Login.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.User')),
            ],
            options={
                'verbose_name': '好友',
                'verbose_name_plural': '好友',
            },
        ),
    ]
