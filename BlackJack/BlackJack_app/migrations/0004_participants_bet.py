# Generated by Django 3.0.5 on 2020-05-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlackJack_app', '0003_auto_20200514_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='bet',
            field=models.IntegerField(default=0),
        ),
    ]
