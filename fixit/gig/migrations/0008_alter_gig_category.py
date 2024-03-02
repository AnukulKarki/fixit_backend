# Generated by Django 5.0 on 2024-02-24 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('gig', '0007_rename_category_gig_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category'),
        ),
    ]