# Generated by Django 3.1.3 on 2020-11-20 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_bakedgood_baked_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakedgood',
            name='baked_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
