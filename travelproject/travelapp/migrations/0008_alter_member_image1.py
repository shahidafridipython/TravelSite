# Generated by Django 4.1.7 on 2023-03-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0007_rename_description_member_description1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image1',
            field=models.ImageField(upload_to='photo'),
        ),
    ]