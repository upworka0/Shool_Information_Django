# Generated by Django 2.1.1 on 2018-11-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0022_auto_20181111_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lrn',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Learner Reference Number'),
        ),
    ]