# Generated by Django 5.0.2 on 2024-02-20 17:07

import django.core.validators
import plants.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('plant_name', models.CharField(max_length=20, validators=[plants.models.validate_plant_name, django.core.validators.MinLengthValidator(2)])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
