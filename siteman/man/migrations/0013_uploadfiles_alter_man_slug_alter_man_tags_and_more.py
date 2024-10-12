# Generated by Django 5.0.7 on 2024-10-12 07:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0012_alter_man_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.AlterField(
            model_name='man',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100)], verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='man',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='man.tagpost', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='man',
            name='wife',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mun', to='man.wife', verbose_name='Супруга'),
        ),
    ]