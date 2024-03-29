# Generated by Django 3.1.7 on 2022-12-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('mail', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('add1', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=10)),
            ],
        ),
    ]
