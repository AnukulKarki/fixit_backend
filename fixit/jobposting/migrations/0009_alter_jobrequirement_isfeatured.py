# Generated by Django 5.0 on 2024-03-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobposting', '0008_alter_jobrequirement_isfeatured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequirement',
            name='isFeatured',
            field=models.BooleanField(default=False),
        ),
    ]