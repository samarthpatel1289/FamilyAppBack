# Generated by Django 4.0.1 on 2022-02-01 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
