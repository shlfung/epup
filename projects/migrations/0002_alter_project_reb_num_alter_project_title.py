# Generated by Django 4.2.3 on 2023-07-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reb_num',
            field=models.CharField(max_length=1000, verbose_name='REB Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Project Title'),
        ),
    ]
