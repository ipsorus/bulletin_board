# Generated by Django 2.2.6 on 2019-10-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(blank=True, max_length=100)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('seller', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('car_description', models.TextField(blank=True)),
                ('car_specs', models.TextField(blank=True)),
                ('avito_item', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]