# Generated by Django 5.1.4 on 2025-02-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_alter_account_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_number',
            field=models.IntegerField(default=0),
        ),
    ]
