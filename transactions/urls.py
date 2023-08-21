from django.urls import path, include
from . import views

urlpatterns = [
    path('add/',views.add_transaction,name="Add Trasntion"),
    path('get/',views.get_all_transaction,name="Add Trasntion"),
]
