# Generated by Django 3.0.5 on 2020-05-17 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200517_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(max_length=111),
        ),
    ]
