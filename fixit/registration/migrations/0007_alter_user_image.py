# Generated by Django 5.0 on 2024-03-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_delete_worker_user_category_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
