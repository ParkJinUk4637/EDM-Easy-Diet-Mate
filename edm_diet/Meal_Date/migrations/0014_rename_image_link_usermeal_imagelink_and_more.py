# Generated by Django 4.2 on 2024-01-04 15:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Meal_Date", "0013_usermealevaluation_sum_col_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usermeal",
            old_name="image_link",
            new_name="imagelink",
        ),
        migrations.RenameField(
            model_name="usermeal",
            old_name="user_id",
            new_name="uuid",
        ),
        migrations.RenameField(
            model_name="usermealevaluation",
            old_name="user_id",
            new_name="uuid",
        ),
    ]