# Generated by Django 3.1.2 on 2021-01-11 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20210111_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetail',
            name='total_no_working_days',
        ),
    ]
