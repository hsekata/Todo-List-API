# Generated by Django 5.1.7 on 2025-03-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_API', '0002_usertodo_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertodo',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertodo',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
