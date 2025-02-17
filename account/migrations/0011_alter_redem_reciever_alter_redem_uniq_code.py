# Generated by Django 5.1.4 on 2025-02-14 10:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_check_bank_alter_check_reciever_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='redem',
            name='reciever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='received_redemptions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='redem',
            name='uniq_code',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
