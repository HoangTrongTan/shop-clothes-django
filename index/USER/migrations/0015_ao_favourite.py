# Generated by Django 4.2 on 2023-06-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0014_ao_temp_tongtien'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ao_favourite',
            fields=[
                ('id_ao', models.IntegerField(primary_key=True, serialize=False)),
                ('ten_ao', models.CharField(max_length=200)),
                ('giatien', models.IntegerField()),
                ('anh', models.CharField(max_length=200)),
                ('taikhoan', models.CharField(max_length=200)),
            ],
        ),
    ]
