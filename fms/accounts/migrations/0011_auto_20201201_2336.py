# Generated by Django 3.1.2 on 2020-12-01 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201201_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_profile',
            name='student',
        ),
        migrations.AddField(
            model_name='payment',
            name='fee_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.fee'),
        ),
        migrations.AddField(
            model_name='payment',
            name='student_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.student'),
        ),
        migrations.AddField(
            model_name='student_profile',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='student_profile',
            name='student_id',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
        migrations.AlterField(
            model_name='fee',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fee',
            name='ayear',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fee',
            name='college_type',
            field=models.CharField(choices=[('GOVT / AIDED', 'GOVT / AIDED'), ('Deemed / PRIV. Univ', 'Deemed / PRIV. Univ'), ('ALL-COLLEGES', 'ALL')], max_length=50),
        ),
        migrations.AlterField(
            model_name='fee',
            name='course',
            field=models.CharField(choices=[('ENGINEERING/ARCHITECTURE', 'ENGINEERING/ARCHITECTURE'), ('ENGINEERING SNQ', 'ENGINEERING SNQ')], max_length=50),
        ),
        migrations.AlterField(
            model_name='fee',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='entry',
            field=models.CharField(choices=[('KCET', 'KCET'), ('COMEDK', 'COMEDK'), ('MANAGEMENT', 'MANAGEMENT')], max_length=20),
        ),
        migrations.AlterField(
            model_name='fee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fee',
            name='quota',
            field=models.CharField(choices=[('GENERAL MERIT', 'GM'), ('OTHER BACKWARD CLASSES', 'OBC'), ('SC/ST', 'SC/ST'), ('CAT-1', (('IC < 2.5 LPA', 'IC < 2.5 LPA'), ('IC > 2.5 LPA', 'IC > 2.5 LPA')))], max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Total_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='mode_payment',
            field=models.CharField(choices=[('NEFT', 'NEFT'), ('BANK-TO-BANK', 'BANK-TO-BANK'), ('NETBANKING', 'NETBANKING')], max_length=25),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pay_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Payment_recieved', 'recieved'), ('Payment_acknowledgement', 'acknowledged')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='ad_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ISE', 'ISE'), ('ME', 'ME'), ('CVE', 'CVE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Aeronautical/ Aerospace Eng', 'AE'), ('Artificial Intelligence Eng', 'AIE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(choices=[('KCET', 'KCET'), ('COMEDK', 'COMEDK'), ('MANAGEMENT', 'MANAGEMENT')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='ed_level',
            field=models.CharField(choices=[('12', '12'), ('DIPLOMA', 'DIPLOMA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='aadhar',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='caste',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='father_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='mother_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='phone1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='phone2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='subcaste',
            field=models.CharField(max_length=20),
        ),
    ]