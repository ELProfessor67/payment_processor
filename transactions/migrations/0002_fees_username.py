# Generated by Django 4.0.6 on 2023-10-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
