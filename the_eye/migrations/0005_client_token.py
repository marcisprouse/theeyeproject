# Generated by Django 4.0 on 2021-12-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_eye', '0004_alter_event_data_alter_event_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
