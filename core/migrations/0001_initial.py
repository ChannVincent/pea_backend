# Generated by Django 4.2.5 on 2023-10-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business",
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
                ("Name", models.CharField(max_length=256)),
                ("symbol", models.CharField(default="", max_length=20, unique=True)),
            ],
        ),
    ]
