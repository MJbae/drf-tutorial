# Generated by Django 3.1.13 on 2021-12-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_squashed_0006_dog_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('dog_set', models.ManyToManyField(blank=True, to='dogs.Dog')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('dog_set', models.ManyToManyField(blank=True, to='dogs.Dog')),
            ],
        ),
    ]
