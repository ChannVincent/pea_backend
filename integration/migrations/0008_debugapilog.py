# Generated by Django 4.2.5 on 2023-10-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("integration", "0007_remove_yahoofinanceintegration_base_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="DebugApiLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now=True)),
                ("url", models.CharField(max_length=256)),
                ("data", models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
