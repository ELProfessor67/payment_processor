# Generated by Django 4.0.6 on 2023-08-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='description',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='status',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='trasnsaction_id',
        ),
        migrations.AddField(
            model_name='transactions',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='card_number',
            field=models.CharField(default='', max_length=16, verbose_name='Card Number'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='city',
            field=models.CharField(default='', max_length=100, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='company',
            field=models.CharField(default='', max_length=100, verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='country',
            field=models.CharField(default='', max_length=100, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='cvv',
            field=models.CharField(default='', max_length=4, verbose_name='CVV'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='email',
            field=models.EmailField(default='', max_length=100, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='exp_month',
            field=models.CharField(default='', max_length=5, verbose_name='Expiration Month'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='exp_year',
            field=models.CharField(default='', max_length=5, verbose_name='Expiration Year'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='first_name',
            field=models.CharField(default='', max_length=100, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='last_name',
            field=models.CharField(default='', max_length=100, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='phone_number',
            field=models.CharField(default='', max_length=20, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='state',
            field=models.CharField(default='', max_length=100, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_id',
            field=models.CharField(default='12', max_length=5, verbose_name='Transaction_id'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_type',
            field=models.CharField(default='', max_length=100, verbose_name='Transaction Type'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='zip_code',
            field=models.CharField(default='', max_length=10, verbose_name='Zip'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='payment_method',
            field=models.CharField(default='', max_length=100),
        ),
    ]
