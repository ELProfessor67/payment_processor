from django.contrib import admin
from django.urls import path, include
from .views import login, about,logoutuser,table,register,api_management
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transation/',include('transactions.urls')),
    path('batch/',include('batchs.urls')),
    path('login/',login,name="login page"),
    path('register/',register,name="register page"),
    path('api/management/',api_management,name="api management"),
    path('logout/',logoutuser,name="logout page"),
    path('code/table',table,name="table"),
    path('',about,name="about page"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
