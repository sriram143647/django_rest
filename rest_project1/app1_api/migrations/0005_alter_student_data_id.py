# Generated by Django 4.1.5 on 2023-01-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_api', '0004_auto_20221227_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
