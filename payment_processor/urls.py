from django.contrib import admin
from django.urls import path, include
from .views import login, about,logoutuser,table
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transation/',include('transactions.urls')),
    path('batch/',include('batchs.urls')),
    path('login/',login,name="login page"),
    path('logout/',logoutuser,name="logout page"),
    path('code/table',table,name="table"),
    path('',about,name="about page"),
]


urlpatterns += staticfiles_urlpatterns()
