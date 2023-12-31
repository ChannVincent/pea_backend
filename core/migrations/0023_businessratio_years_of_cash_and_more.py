# Generated by Django 4.2.5 on 2023-10-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0022_businessratio"),
    ]

    operations = [
        migrations.AddField(
            model_name="businessratio",
            name="years_of_cash",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                default=None,
                help_text="percent",
                max_digits=10,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="businessratio",
            name="years_to_repay_debt",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                default=None,
                help_text="percent",
                max_digits=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="businessratio",
            name="net_margin",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                default=None,
                help_text="percent",
                max_digits=6,
                null=True,
            ),
        ),
    ]
