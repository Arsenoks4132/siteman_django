# Generated by Django 4.2.1 on 2024-07-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0002_alter_man_options_man_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='man',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
