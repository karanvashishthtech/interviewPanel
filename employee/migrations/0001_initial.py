# Generated by Django 4.0.4 on 2022-05-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Complete', 'Complete'), ('In progress', 'In progress'), ('Pending', 'Pending')], default='Pending', max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('MobileNumber', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
            ],
        ),
    ]