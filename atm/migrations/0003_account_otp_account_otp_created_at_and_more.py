# Generated by Django 5.0.6 on 2024-08-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0002_account_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='otp',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='otp_created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.PositiveBigIntegerField(max_length=10),
        ),
    ]
