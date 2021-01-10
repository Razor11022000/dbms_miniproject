# Generated by Django 3.1.2 on 2021-01-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20210108_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ad_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MALE', 'M'), ('FEMALE', 'F'), ('OTHER', 'O')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile_pic.png', null=True, upload_to=''),
        ),
    ]
