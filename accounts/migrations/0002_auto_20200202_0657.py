# Generated by Django 3.0.2 on 2020-02-02 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='addrress',
            new_name='address',
        ),
    ]
