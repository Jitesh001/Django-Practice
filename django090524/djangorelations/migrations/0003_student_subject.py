# Generated by Django 5.0.6 on 2024-05-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorelations', '0002_singer_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('total_marks', models.IntegerField()),
                ('student', models.ManyToManyField(to='djangorelations.student')),
            ],
        ),
    ]