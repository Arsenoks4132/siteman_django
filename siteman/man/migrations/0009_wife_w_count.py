# Generated by Django 4.2.1 on 2024-07-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0008_wife_man_wife'),
    ]

    operations = [
        migrations.AddField(
            model_name='wife',
            name='w_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
