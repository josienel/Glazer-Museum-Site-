# Generated by Django 5.0.1 on 2024-04-09 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_rename_activity_id_activity_activity_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('exhibit_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ex_name', models.CharField(max_length=255)),
                ('ex_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.activity')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.play')),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.exhibit')),
            ],
        ),
    ]