# Generated by Django 4.1.7 on 2023-04-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
