# Generated by Django 3.0.5 on 2020-04-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAHADEV', '0002_auto_20200429_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='Name',
            field=models.CharField(default='Name', max_length=100),
            preserve_default=False,
        ),
    ]