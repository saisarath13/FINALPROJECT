# Generated by Django 3.0.5 on 2020-04-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAHADEV', '0007_auto_20200430_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geeksmodel',
            name='Event_name',
        ),
        migrations.AddField(
            model_name='geeksmodel',
            name='EEvent_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]