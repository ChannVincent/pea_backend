# Generated by Django 4.2.5 on 2023-10-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_business_country_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="business",
            name="last_update",
            field=models.DateTimeField(null=True),
        ),
    ]
