# Generated by Django 4.0 on 2021-12-23 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('the_eye', '0005_client_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='session_id',
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(blank=True, max_length=255, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='the_eye.event')),
            ],
        ),
    ]
