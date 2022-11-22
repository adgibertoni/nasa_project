# Generated by Django 4.1.2 on 2022-11-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0003_alter_top10_options_alter_top10_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='top10',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='top10',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='top10'),
        ),
        migrations.AddField(
            model_name='top10',
            name='year',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterUniqueTogether(
            name='top10',
            unique_together={('title', 'year')},
        ),
    ]