# Generated by Django 3.2.16 on 2022-11-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oshuApp', '0002_remove_profile_userdd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinformation',
            name='EventID',
            field=models.TextField(unique=True),
        ),
    ]