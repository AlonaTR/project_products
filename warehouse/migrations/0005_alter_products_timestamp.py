# Generated by Django 3.2.11 on 2022-07-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_auto_20220711_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]