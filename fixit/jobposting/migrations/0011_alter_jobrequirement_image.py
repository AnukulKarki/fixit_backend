# Generated by Django 5.0 on 2024-03-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobposting', '0010_alter_jobrequirement_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequirement',
            name='image',
            field=models.ImageField(null=True, upload_to='image/jobreq'),
        ),
    ]
