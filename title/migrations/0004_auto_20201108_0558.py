# Generated by Django 3.0.5 on 2020-11-08 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0003_auto_20201102_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, related_name='genre_titles', to='title.Genre'),
        ),
    ]