# Generated by Django 4.2.5 on 2023-10-13 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("integration", "0008_debugapilog"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DebugApiLog",
        ),
    ]
