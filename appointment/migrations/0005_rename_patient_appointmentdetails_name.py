# Generated by Django 4.2.2 on 2023-06-29 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0004_remove_appointmentdetails_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointmentdetails",
            old_name="patient",
            new_name="name",
        ),
    ]
