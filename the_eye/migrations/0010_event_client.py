# Generated by Django 4.0 on 2021-12-24 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('the_eye', '0009_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='the_eye.client'),
        ),
    ]
