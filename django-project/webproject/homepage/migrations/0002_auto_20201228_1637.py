# Generated by Django 2.2.5 on 2020-12-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='id',
        ),
        migrations.AlterField(
            model_name='coffee',
            name='name',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]
