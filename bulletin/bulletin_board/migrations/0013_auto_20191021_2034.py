# Generated by Django 2.2.6 on 2019-10-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0012_auto_20191020_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_brand',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_title',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_of_manufacture',
            field=models.IntegerField(db_index=True, null=True),
        ),
    ]
