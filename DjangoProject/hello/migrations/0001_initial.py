# Generated by Django 5.0.1 on 2024-04-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('play_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('play_type', models.CharField(max_length=100)),
                ('play_desc', models.TextField()),
            ],
        ),
    ]
