# Generated by Django 4.1.6 on 2023-03-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(),
        ),
    ]