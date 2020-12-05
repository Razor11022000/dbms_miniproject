# Generated by Django 3.1.2 on 2020-12-01 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201201_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.student')),
                ('email', models.EmailField(max_length=50, null=True)),
                ('father_name', models.CharField(blank=True, default=True, max_length=50)),
                ('mother_name', models.CharField(blank=True, default=True, max_length=50)),
                ('phone1', models.CharField(blank=True, default=True, max_length=20)),
                ('phone2', models.CharField(blank=True, default=True, max_length=20)),
                ('address', models.CharField(blank=True, default=True, max_length=200)),
                ('photo', models.ImageField(blank=True, default=True, upload_to='images/')),
                ('dob', models.DateField(null=True)),
                ('caste', models.CharField(blank=True, default=True, max_length=20)),
                ('subcaste', models.CharField(blank=True, default=True, max_length=20)),
                ('aadhar', models.CharField(blank=True, default=True, max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Student_personal',
        ),
        migrations.AlterField(
            model_name='fee',
            name='college_type',
            field=models.CharField(choices=[('GOVT / AIDED', 'GOVT / AIDED'), ('Deemed / PRIV. Univ', 'Deemed / PRIV. Univ'), ('ALL-COLLEGES', 'ALL')], max_length=50, null=True),
        ),
    ]
