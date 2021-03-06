# Generated by Django 3.1 on 2020-08-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('gender', models.CharField(default='F', max_length=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('marital_stat', models.CharField(default='S', max_length=1)),
                ('job_stat', models.CharField(default='S', max_length=1)),
                ('mobile_no', models.CharField(default='', max_length=15)),
                ('email_id', models.CharField(default='', max_length=100)),
                ('house_name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=200)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Expdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_head', models.IntegerField(default=1)),
                ('exp_details', models.CharField(blank=True, default='', max_length=200)),
                ('created_on', models.DateTimeField(auto_now=True, null=True)),
                ('edited_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exphead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_head', models.CharField(default='', max_length=70)),
                ('db_cr', models.CharField(blank=True, default='DB', max_length=2)),
                ('created_on', models.DateTimeField(auto_now=True, null=True)),
                ('edited_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Homehead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('gender', models.CharField(default='F', max_length=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('marital_stat', models.CharField(default='S', max_length=1)),
                ('husband_code', models.CharField(default=' ', max_length=2)),
                ('children_no', models.CharField(default='0', max_length=2)),
                ('job_stat', models.CharField(default='S', max_length=1)),
                ('mobile_no', models.CharField(default='', max_length=15)),
                ('email_id', models.CharField(default='', max_length=100)),
                ('house_name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=200)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trn_no', models.CharField(default='', max_length=70)),
                ('trn_date', models.DateField(auto_now=True)),
                ('trn_type', models.CharField(default='DB', max_length=2)),
                ('trn_head', models.IntegerField(default=0)),
                ('trn_amt', models.FloatField(blank=True, default=0.0)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('edited_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('address', models.CharField(default='', max_length=200)),
                ('mobileno', models.CharField(default='', max_length=20)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
