# Generated by Django 4.0.4 on 2022-07-04 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_data',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='hobby1',
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='hobby2',
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='hobby3',
        ),
    ]
