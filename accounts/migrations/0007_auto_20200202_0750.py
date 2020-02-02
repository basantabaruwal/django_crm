# Generated by Django 3.0.2 on 2020-02-02 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200202_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Product'),
        ),
    ]
