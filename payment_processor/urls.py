from django.contrib import admin
from django.urls import path, include
from .views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transation/',include('transactions.urls')),
    path('',home,name="home page"),
]


urlpatterns += staticfiles_urlpatterns()
