from django.db import models

from django.db import models
import datetime
from math import trunc
import re


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
    owner = models.CharField(max_length=100)
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
        fee_model = Fees.objects.filter(username=self.owner).first()
        if fee_model == None:
            # print(fee_model)
            fee_model = Fees(percent=2.5,flat_fee=0.5)
            # fee_model['percent'] = 2.5
            # fee_model['flat_fee'] = 0.5
            
        percent = (float(self.amount)*float(fee_model.percent))/100
        fee = round(((percent*100)-float(fee_model.flat_fee))/100)
        self.p_fee = fee
        # print(self.amount,self.p_fee,self.g_fee)
        self.amount = trunc(float(self.amount)-(self.p_fee+self.g_fee))
        return self



    def get_codes(self):
        if self.country.lower() != 'usa':
            self.transaction_type = f"{self.transaction_type}-international"
            # print(self.transaction_type)
        
        if codes.get(self.transaction_type):
            self.codes = codes.get(self.transaction_type)
        else:
            self.codes = {
                "code": "219248",
                "transaction_type": "7128"
            }
        return self
    

    def get_card_company(self):
        card_number = self.card_number
        # Define regular expressions for different card companies
        patterns = {
            'Visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
            'Mastercard': r'^5[1-5][0-9]{14}$',
            "Amex": r'^3[47][0-9]{13}$',
            "Discover": r'^6(?:011|5[0-9]{2})[0-9]{12}$',
            "JCB": r'^(?:2131|1800|35[0-9]{3})[0-9]{11}$'
            # Add more patterns for other card companies here
        }

        for company, pattern in patterns.items():
            if re.match(pattern, card_number):
                return company
        # If no company is detected, return 'unknown'
        return 'Amex'


class Fees(models.Model):
    
    percent = models.FloatField()
    flat_fee = models.FloatField()
    username = models.CharField(max_length=200, default='')

