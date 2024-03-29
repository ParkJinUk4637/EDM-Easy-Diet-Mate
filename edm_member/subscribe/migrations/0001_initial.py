# Generated by Django 4.2 on 2024-01-02 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subscribe_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_subscribe', to=settings.AUTH_USER_MODEL, to_field='uuid')),
                ('subscribe_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_subscribe', to=settings.AUTH_USER_MODEL, to_field='uuid')),
            ],
            options={
                'verbose_name': '구독',
                'verbose_name_plural': '구독 목록',
                'unique_together': {('subscribe_from', 'subscribe_to')},
            },
        ),
    ]
