# Generated by Django 4.2 on 2024-01-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0002_cardnews"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardnews",
            name="link",
            field=models.URLField(default="", max_length=250, verbose_name="링크"),
        ),
    ]
