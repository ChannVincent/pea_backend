# Generated by Django 4.2.5 on 2023-10-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_yearlyreport_capital_expenditure_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quarterreport",
            name="earning",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="quarterreport",
            name="revenue",
            field=models.IntegerField(default=None, null=True),
        ),
    ]
