# Generated by Django 4.1.7 on 2023-03-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualifications_Name', models.CharField(max_length=10)),
            ],
        ),
    ]
