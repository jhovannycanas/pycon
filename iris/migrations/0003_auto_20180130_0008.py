# Generated by Django 2.0 on 2018-01-30 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iris', '0002_auto_20180129_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='classification',
            field=models.CharField(default=None, max_length=25, null=True),
        ),
    ]
