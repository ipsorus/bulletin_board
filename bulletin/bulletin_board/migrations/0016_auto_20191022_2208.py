# Generated by Django 2.2.6 on 2019-10-22 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0015_auto_20191022_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='image',
            new_name='image_data_link',
        ),
    ]