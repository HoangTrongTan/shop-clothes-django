# Generated by Django 4.2 on 2023-05-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0003_remove_ao_anh_lq_delete_loaianh'),
    ]

    operations = [
        migrations.AddField(
            model_name='ao',
            name='old_image',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]