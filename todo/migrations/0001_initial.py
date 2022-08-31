# Generated by Django 4.1 on 2022-08-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=70)),
                (
                    "description",
                    models.TextField(
                        choices=[
                            ("C", "Completed"),
                            ("P", "Pending"),
                            ("I", "In-Progress"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("1", "1️⃣"),
                            ("2", "2️⃣"),
                            ("3", "3️⃣"),
                            ("4", "4️⃣"),
                            ("5", "5️⃣"),
                        ],
                        max_length=2,
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
