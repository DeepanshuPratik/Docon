# Generated by Django 3.2.3 on 2021-06-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210615_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='data',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
