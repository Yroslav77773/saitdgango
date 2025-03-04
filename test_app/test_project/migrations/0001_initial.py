# Generated by Django 5.1.5 on 2025-03-04 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('car_brand', models.CharField(max_length=255)),
                ('car_body', models.CharField(max_length=255)),
                ('horse_power', models.IntegerField()),
                ('car_drive', models.CharField(max_length=255)),
                ('tax', models.FloatField(default=0)),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=255)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='test_project.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('author_id', models.IntegerField(default=0)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='test_project.car')),
            ],
        ),
    ]
