# Generated by Django 2.2.5 on 2020-12-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20201228_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='is_ice',
        ),
        migrations.AddField(
            model_name='coffee',
            name='stock',
            field=models.IntegerField(default=5),
        ),
    ]
