# Generated by Django 3.0.5 on 2020-04-04 20:15

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0003_auto_20200404_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='publication_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
        ),
    ]
