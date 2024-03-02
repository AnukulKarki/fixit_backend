# Generated by Django 5.0 on 2024-02-24 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('jobposting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequirement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobreq_category', to='category.category'),
        ),
    ]
