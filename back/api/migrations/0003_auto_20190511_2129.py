# Generated by Django 2.2.1 on 2019-05-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190511_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=700),
        ),
    ]