# Generated by Django 4.0 on 2021-12-22 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_eye', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
