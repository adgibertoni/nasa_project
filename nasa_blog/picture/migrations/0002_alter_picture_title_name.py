# Generated by Django 4.1.2 on 2022-11-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='title_name',
            field=models.CharField(max_length=80),
        ),
    ]