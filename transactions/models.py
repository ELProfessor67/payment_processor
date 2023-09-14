from django.db import models

from django.db import models
import datetime
from math import trunc


codes = {
    "charge": {
        "code": "00",
        "transaction_type": "101"
    },
    "charge-international": {
        "code": "003100",
        "transaction_type": "102"
    },
    "refund": {
        "code":  "0001",
        "transaction_type": "503"
    },
    "refund-international": {
        "code": "003101",
        "transaction_type": "508"
    },
    "save": {
        "code":  "219248",
        "transaction_type": "7128"
    },
    "save-international": {
        "code": "219248",
        "transaction_type": "7128"
    },
    "post-only": {
        "code":  "219248",
        "transaction_type": "7128"
    },
    "post-only-international": {
        "code": "219248",
        "transaction_type": "7128"
    },
    "auth-only": {
        "code":  "219248",
        "transaction_type": "7128"
    },
    "auth-only-international": {
        "code": "219248",
        "transaction_type": "7128"
    },

}

class Transactions(models.Model):
    username = models.CharField(max_length=100, verbose_name='Username',default='')
    first_name = models.CharField(max_length=100, verbose_name='First Name',default='')
    last_name = models.CharField(max_length=100, verbose_name='Last Name',default='')
    company = models.CharField(max_length=100, verbose_name='Company',default='')
    address = models.CharField(max_length=100, verbose_name='Address',default='')
    city = models.CharField(max_length=100, verbose_name='City',default='')
    state = models.CharField(max_length=100, verbose_name='State',default='')
    zip_code = models.CharField(max_length=10, verbose_name='Zip',default='')
    country = models.CharField(max_length=100, verbose_name='Country',default='')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number',default='')
    amount = models.CharField(max_length=100,default='')
    payment_method = models.CharField(max_length=100,default='')
    transaction_type = models.CharField(max_length=100, verbose_name='Transaction Type',default='')
    card_number = models.CharField(max_length=16, verbose_name='Card Number' ,default='')
    exp_year = models.CharField(max_length=5, verbose_name='Expiration Year',default='')
    exp_month = models.CharField(max_length=5, verbose_name='Expiration Month',default='')
    cvv = models.CharField(max_length=4, verbose_name='CVV',default='')
    email = models.EmailField(max_length=100, verbose_name='Email',default='')
    transaction_id = models.CharField(max_length=150, verbose_name='Transaction_id',default='')
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def cut_fee(self):
        self.g_fee = float(self.amount)/100
        fee_model = Fees.objects.all().first()
        percent = (float(self.amount)*float(fee_model.percent))/100
        fee = round(((percent*100)-float(fee_model.flat_fee))/100)
        self.p_fee = fee
        print(self.amount,self.p_fee,self.g_fee)
        self.amount = trunc(float(self.amount)-(self.p_fee+self.g_fee))
        return self



    def get_codes(self):
        if self.country.lower() != 'usa':
            self.transaction_type = f"{self.transaction_type}-international"
        
        if codes.get(self.transaction_type):
            self.codes = codes.get(self.transaction_type)
        else:
            self.codes = {
                "code": "219248",
                "transaction_type": "7128"
            }
        return self


class Fees(models.Model):
    
    percent = models.FloatField()
    flat_fee = models.FloatField()

