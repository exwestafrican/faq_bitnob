# Generated by Django 3.0.7 on 2020-07-15 02:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="phone numbers need to come with extentions, e.g +23481690....",
                max_length=128,
                null=True,
                region=None,
            ),
        ),
    ]
