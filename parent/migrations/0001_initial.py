# Generated by Django 3.2 on 2023-11-24 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prntdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prntName', models.CharField(max_length=250)),
                ('prntMailid', models.EmailField(max_length=150)),
                ('prntphone_no', models.IntegerField(default=0)),
                ('Feepaid', models.IntegerField(default=0)),
                ('Feedue', models.IntegerField(default=0)),
            ],
        ),
    ]
