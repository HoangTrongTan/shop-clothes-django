# Generated by Django 4.2 on 2023-05-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ao',
            name='anh',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
