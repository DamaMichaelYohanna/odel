# Generated by Django 3.0.8 on 2024-09-08 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0005_auto_20240908_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, max_length=10, null=True)),
                ('is_current', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second')], max_length=10, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='programme.Session')),
            ],
        ),
    ]