# Generated by Django 2.1.1 on 2018-11-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0012_auto_20181109_0225'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Section',
            new_name='Class',
        ),
        migrations.AlterField(
            model_name='student',
            name='lrn',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='Learner Reference Number'),
        ),
    ]

    atomic = False
