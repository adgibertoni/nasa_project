# Generated by Django 4.1.2 on 2022-11-18 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_alter_picture_title_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['-taken_date']},
        ),
    ]