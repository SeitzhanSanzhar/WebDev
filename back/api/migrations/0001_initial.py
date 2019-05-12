# Generated by Django 2.1.7 on 2019-05-10 18:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(default='Klassika', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Klassika', max_length=100)),
                ('body', models.CharField(default='Klassika', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_info', models.ForeignKey(on_delete=None, to='api.Book')),
                ('created_by', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]