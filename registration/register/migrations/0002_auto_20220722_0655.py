# Generated by Django 3.1.7 on 2022-07-22 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
