# Generated by Django 4.2.5 on 2023-10-16 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_businessevent"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DebugApiLog",
        ),
    ]
