# Generated by Django 3.1.13 on 2021-11-20 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(null=True)),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
            ],
        ),
    ]
