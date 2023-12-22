# Generated by Django 4.2 on 2023-12-22 05:49

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(default="", max_length=100, unique=True)),
                ("name", models.CharField(default="", max_length=10)),
                ("birthdate", models.DateField(default=django.utils.timezone.now)),
                (
                    "active_level",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                        ],
                        default="level 1",
                        max_length=7,
                    ),
                ),
                ("height", models.SmallIntegerField(default=0)),
                ("weight", models.SmallIntegerField(default=0)),
                (
                    "diet_purpose",
                    models.CharField(
                        choices=[
                            ("체중 감량", "체중 감량"),
                            ("체중 유지", "체중 유지"),
                            ("체중 증량", "체중 증량"),
                        ],
                        default="체중 유지",
                        max_length=11,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("남자", "남자"), ("여자", "여자")], max_length=5
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
