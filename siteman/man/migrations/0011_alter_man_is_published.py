# Generated by Django 5.0.7 on 2024-07-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0010_alter_category_options_alter_man_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='man',
            name='is_published',
            field=models.CharField(choices=[('DRAFT', 'Черновик'), ('PUBLISHED', 'Опубликовано')], default='DRAFT', max_length=20, verbose_name='Опубликовано'),
        ),
    ]