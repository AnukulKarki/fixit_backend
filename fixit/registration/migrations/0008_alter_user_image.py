# Generated by Django 5.0 on 2024-03-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='image/citizenship'),
        ),
    ]
