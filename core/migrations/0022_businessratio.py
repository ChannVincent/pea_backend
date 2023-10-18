# Generated by Django 4.2.5 on 2023-10-18 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_alter_businessinfo_business"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessRatio",
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
                    "market_cap",
                    models.IntegerField(blank=True, default=None, null=True),
                ),
                (
                    "net_margin",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=None,
                        max_digits=6,
                        null=True,
                    ),
                ),
                (
                    "cash_position",
                    models.IntegerField(blank=True, default=None, null=True),
                ),
                ("debt", models.IntegerField(blank=True, default=None, null=True)),
                ("revenue", models.IntegerField(blank=True, default=None, null=True)),
                ("earnings", models.IntegerField(blank=True, default=None, null=True)),
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
