# Generated by Django 4.2.7 on 2024-01-16 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knedlicky', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='play',
            new_name='mood',
        ),
        migrations.RemoveField(
            model_name='post',
            name='play2',
        ),
    ]
