# Generated by Django 5.1.4 on 2024-12-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='uploadedimage',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]