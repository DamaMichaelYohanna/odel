# Generated by Django 3.0.8 on 2024-09-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20240901_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='home_town',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='relation',
        ),
        migrations.AddField(
            model_name='student',
            name='has_accepted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_admitted',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='kin_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='kin_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='kin_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='kin_relation',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='programme_type',
            field=models.CharField(blank=True, default='Part Time', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='year_of_admission',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='app_id',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_country',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_lga',
            field=models.CharField(blank=True, max_length=205, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='lga',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='marital_status',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mat_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]