# Generated by Django 2.1.1 on 2018-11-07 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_auto_20181105_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
    ]
