# Generated by Django 2.1.1 on 2018-11-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0024_auto_20181111_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='grade_level',
            field=models.CharField(choices=[('K', 'Kinder'), ('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI')], max_length=1),
        ),
    ]