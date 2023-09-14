from django.urls import path, include
from . import views

urlpatterns = [
    path('add/',views.add_transaction,name="Add Trasntion"),
    path('get/',views.get_all_transaction,name="Add Trasntion"),
    path('list/',views.user_show_list,name="show list"),
    path('fee/',views.fee,name="cutomize fee"),
    path('list/<str:username>',views.user_transaction,name="show list"),
]
