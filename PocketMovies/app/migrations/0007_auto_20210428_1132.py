# Generated by Django 3.1.7 on 2021-04-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210428_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='imageField',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='imageField',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imageField',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='producer',
            name='imageField',
            field=models.URLField(blank=True),
        ),
    ]