# Generated by Django 2.0.5 on 2018-06-14 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_type',
            new_name='song_title',
        ),
    ]