# Generated by Django 3.1.2 on 2020-12-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201130_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=50, null=True)),
                ('mother_name', models.CharField(max_length=50, null=True)),
                ('phone1', models.CharField(max_length=20, null=True)),
                ('phone2', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to='images/')),
                ('dob', models.DateField(null=True)),
                ('caste', models.CharField(max_length=20, null=True)),
                ('subcaste', models.CharField(max_length=20, null=True)),
                ('aadhar', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='fee',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='fee',
            name='category',
        ),
        migrations.RemoveField(
            model_name='fee',
            name='fid',
        ),
        migrations.RemoveField(
            model_name='pay',
            name='fid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='aadhar',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ad_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='caste',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone1',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone2',
        ),
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='student',
            name='subcaste',
        ),
        migrations.AddField(
            model_name='fee',
            name='entry',
            field=models.CharField(choices=[('KCET', 'KCET'), ('COMEDK', 'COMEDK'), ('MANAGEMENT', 'MANAGEMENT')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fee',
            name='quota',
            field=models.CharField(choices=[('GENERAL MERIT', 'GM'), ('OTHER BACKWARD CLASSES', 'OBC'), ('SC/ST', 'SC/ST'), ('CAT-1', (('IC < 2.5 LPA', 'IC < 2.5 LPA'), ('IC > 2.5 LPA', 'IC > 2.5 LPA')))], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pay',
            name='Total_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pay',
            name='amount_paid',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pay',
            name='mode_payment',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='category',
            field=models.CharField(choices=[('KCET', 'KCET'), ('COMEDK', 'COMEDK'), ('MANAGEMENT', 'MANAGEMENT')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='ed_level',
            field=models.CharField(choices=[('12', '12'), ('DIPLOMA', 'DIPLOMA')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sem',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ISE', 'ISE'), ('ME', 'ME'), ('CVE', 'CVE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Aeronautical/ Aerospace Eng', 'AE'), ('Artificial Intelligence Eng', 'AIE')], max_length=50, null=True),
        ),
    ]
