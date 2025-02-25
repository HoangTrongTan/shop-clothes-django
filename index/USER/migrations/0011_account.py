# Generated by Django 4.2 on 2023-05-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0010_ao_temp_taikhoan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id_taikhoan', models.AutoField(primary_key=True, serialize=False)),
                ('acc_name', models.CharField(max_length=100)),
                ('pass_user', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('email_user', models.CharField(max_length=200)),
                ('owner_img', models.ImageField(default=None, upload_to='images')),
            ],
        ),
    ]
