# Generated by Django 2.2.6 on 2019-10-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='avito_item',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_specs',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='seller',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]