# Generated by Django 4.2.6 on 2023-10-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=100)),
                ('option', models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], max_length=100)),
            ],
        ),
    ]
