# Generated by Django 2.2.6 on 2019-10-20 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0011_auto_20191020_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
