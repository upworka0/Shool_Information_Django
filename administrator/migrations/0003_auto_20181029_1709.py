# Generated by Django 2.1.1 on 2018-10-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_auto_20181029_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='grade_level',
            field=models.CharField(choices=[('I', '1'), ('II', '2'), ('III', '3'), ('IV', '4'), ('V', '5'), ('VI', '6')], max_length=1),
        ),
    ]
