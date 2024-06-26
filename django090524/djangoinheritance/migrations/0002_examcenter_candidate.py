# Generated by Django 5.0.6 on 2024-05-02 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoinheritance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('city_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('examcenter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='djangoinheritance.examcenter')),
                ('name', models.CharField(max_length=100)),
                ('sr_number', models.IntegerField()),
            ],
            bases=('djangoinheritance.examcenter',),
        ),
    ]
