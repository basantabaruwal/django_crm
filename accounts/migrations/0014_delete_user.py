# Generated by Django 3.0.2 on 2020-02-03 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
