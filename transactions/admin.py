from django.contrib import admin
from transactions.models import Transactions,Fees
# Register your models here.


class TransactionsAdmin(admin.ModelAdmin):
    # list_display=('trasnsaction_id','description','timestamp','currency','payment_method','status','amount')
    list_display=('first_name','last_name','company','address','city','state','zip_code','country','phone_number','amount','payment_method','transaction_type','card_number','exp_year','exp_month','cvv','email','transaction_id','created_at','username')
    search_fields = ('first_name','last_name','company','address','city','state','zip_code','country','phone_number','amount','payment_method','transaction_type','card_number','exp_year','exp_month','cvv','email','transaction_id','created_at','username')
    list_filter = ['created_at']
admin.site.register(Transactions,TransactionsAdmin)
admin.site.register(Fees)