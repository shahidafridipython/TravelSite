# Generated by Django 4.1.7 on 2023-03-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Image', models.ImageField(upload_to='pics')),
                ('Desciption', models.TextField()),
            ],
        ),
    ]
