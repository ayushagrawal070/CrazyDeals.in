# Generated by Django 3.0.5 on 2020-05-17 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200517_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]