# Generated by Django 3.0.5 on 2020-04-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_music_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]
