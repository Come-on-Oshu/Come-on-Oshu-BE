# Generated by Django 3.2.16 on 2022-11-01 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oshuApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventinformation',
            old_name='pid',
            new_name='lid',
        ),
        migrations.RemoveField(
            model_name='eventinformation',
            name='WebsiteUrl',
        ),
    ]