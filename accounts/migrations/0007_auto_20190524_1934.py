# Generated by Django 2.1.8 on 2019-05-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190524_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='like_mate1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_mate2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_mate3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_mate4',
            field=models.IntegerField(default=0),
        ),
    ]
