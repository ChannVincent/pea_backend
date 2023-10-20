# Generated by Django 4.2.5 on 2023-10-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_alter_businessratio_years_of_cash_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="businessratio",
            name="depreciation",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="businessratio",
            name="operating_cash_flow",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="businessratio",
            name="year",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
