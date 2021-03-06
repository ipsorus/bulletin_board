# Generated by Django 2.2.6 on 2019-10-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0003_auto_20191015_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_specs',
        ),
        migrations.AddField(
            model_name='car',
            name='car_brand',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='car_generation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='car_mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='condition',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='drive',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_volume',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='equipment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='car',
            name='modif',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='steering_side',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='type_chassis',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='view_place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='vin_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='year_of_manufacture',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
