# Generated by Django 3.1.2 on 2021-01-11 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20210109_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionYearModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start_year', models.DateField(blank=True, null=True)),
                ('total_no_working_days', models.IntegerField(blank=True, null=True)),
                ('session_end_year', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='TC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendence', models.IntegerField(null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='session_year_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.sessionyearmodel'),
        ),
    ]