# Generated by Django 4.2.5 on 2023-10-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("device_management", "0002_alter_devices_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devices",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
