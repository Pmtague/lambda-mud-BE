# Generated by Django 3.0.3 on 2020-02-07 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_room_room_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_id',
        ),
    ]
