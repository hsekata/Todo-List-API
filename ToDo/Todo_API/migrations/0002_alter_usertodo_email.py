# Generated by Django 5.1.6 on 2025-02-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertodo',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
