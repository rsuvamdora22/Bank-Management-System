# Generated by Django 5.1.4 on 2024-12-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0005_alter_account_encrypted_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='encrypted_pin',
            field=models.CharField(max_length=4),
        ),
    ]