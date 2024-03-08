# Generated by Django 5.0.2 on 2024-02-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=18),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
