# Generated by Django 4.2.8 on 2023-12-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=250, unique_for_date='publish'),
        ),
    ]
