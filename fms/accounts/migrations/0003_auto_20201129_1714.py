# Generated by Django 3.1.2 on 2020-11-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201128_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=20, null=True)),
                ('category', models.CharField(choices=[('College-fees', 'College fees'), ('Miscleneous-fees', 'Miscleneous fees'), ('University-fees', 'University fees')], max_length=50, null=True)),
                ('branch', models.CharField(max_length=20, null=True)),
                ('amount', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('ayear', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Payment_recieved', 'recieved'), ('Payment_acknowledgement', 'acknowledged')], max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='ad_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
