# Generated by Django 3.0.5 on 2020-04-27 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='released',
        ),
    ]