# Generated by Django 4.2.5 on 2023-10-16 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_marketprice"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessEvent",
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
                (
                    "amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=3,
                        default=None,
                        max_digits=14,
                        null=True,
                    ),
                ),
                ("date", models.DateTimeField(blank=True, null=True)),
                ("type", models.CharField(max_length=256)),
                (
                    "data",
                    models.DecimalField(
                        blank=True,
                        decimal_places=3,
                        default=None,
                        max_digits=14,
                        null=True,
                    ),
                ),
                (
                    "business",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.business",
                    ),
                ),
            ],
        ),
    ]
