# Generated by Django 4.2 on 2023-05-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_account',
            fields=[
                ('email', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=100)),
            ],
        ),
    ]
