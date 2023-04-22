# Generated by Django 4.1.6 on 2023-04-22 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Dog",
            fields=[
                (
                    "picture_d",
                    models.ImageField(blank=True, null=True, upload_to="pet_images"),
                ),
                ("age_d", models.IntegerField(default=0)),
                ("name_d", models.CharField(default=" ", max_length=200)),
                ("location_d", models.CharField(default=" ", max_length=200)),
                ("color_d", models.CharField(default=" ", max_length=50)),
                ("description_d", models.TextField(default=" ", max_length=1000)),
                ("date_d", models.DateTimeField(default=django.utils.timezone.now)),
                ("breed_d", models.CharField(default=" ", max_length=200)),
                (
                    "gender_d",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        default=" ",
                        max_length=1,
                    ),
                ),
                ("id", models.AutoField(default=1, primary_key=True, serialize=False)),
                (
                    "username",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cat",
            fields=[
                (
                    "picture_c",
                    models.ImageField(blank=True, null=True, upload_to="pet_images"),
                ),
                ("age_c", models.IntegerField(default=0)),
                ("name_c", models.CharField(default=" ", max_length=200)),
                ("location_c", models.CharField(default=" ", max_length=200)),
                ("color_c", models.CharField(default=" ", max_length=50)),
                ("description_c", models.TextField(default=" ", max_length=1000)),
                ("date_c", models.DateTimeField(default=django.utils.timezone.now)),
                ("breed_c", models.CharField(default=" ", max_length=200)),
                (
                    "gender_c",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        default=" ",
                        max_length=1,
                    ),
                ),
                ("id", models.AutoField(default=1, primary_key=True, serialize=False)),
                (
                    "username",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]