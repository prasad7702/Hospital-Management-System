# Generated by Django 4.2.3 on 2023-10-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Mobile', models.BigIntegerField()),
                ('Address', models.CharField(max_length=500)),
                ('Problem', models.CharField(max_length=50)),
                ('DoctorName', models.CharField(max_length=50)),
            ],
        ),
    ]