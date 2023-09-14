from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.batch_list, name="batchs list"),
    path('create/',views.create_batch, name="batchs create"),
    path('list/<int:id>',views.batch_transaction_list, name="batchs create"),
    path('change_status/<int:id>',views.change_status, name="batchs create"),
]
