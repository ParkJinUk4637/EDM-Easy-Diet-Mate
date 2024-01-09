# Generated by Django 4.2 on 2024-01-03 01:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("Meal_Date", "0002_nutrient_food_id_alter_usermeal_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermeal",
            name="user_id",
            field=models.CharField(default=uuid.uuid4, max_length=32),
        ),
    ]
