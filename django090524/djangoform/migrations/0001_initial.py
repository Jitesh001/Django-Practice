# Generated by Django 5.0.6 on 2024-05-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('roll_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
