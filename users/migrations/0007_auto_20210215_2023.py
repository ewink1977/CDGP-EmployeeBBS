# Generated by Django 3.1.6 on 2021-02-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210215_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertimemanagement',
            name='time_in',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertimemanagement',
            name='time_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
