# Generated by Django 4.2.6 on 2023-10-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_jobpost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
    ]