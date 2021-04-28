# Generated by Django 3.1.7 on 2021-04-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210428_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='imageField',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='director',
            name='imageField',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imageField',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='producer',
            name='imageField',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
