# Generated by Django 4.0 on 2021-12-23 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_eye', '0008_alter_event_category_alter_event_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='event',
            order_with_respect_to='timestamp',
        ),
    ]
