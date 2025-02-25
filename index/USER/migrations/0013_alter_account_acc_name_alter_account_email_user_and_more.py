# Generated by Django 4.2 on 2023-05-31 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0012_alter_account_acc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acc_name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email_user',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='owner_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='pass_user',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
