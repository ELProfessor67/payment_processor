from django.contrib import admin
from django.urls import path, include
from .views import login, dashboard,logoutuser,table,register,api_management,my_team,my_team_add,delete_my,send_mail
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
    path('my/team/',my_team,name="my team"),
    path('my/team/add/',my_team_add,name="my team add"),
    path('my/team/delete/<int:id>',delete_my,name="my team delete"),
    path('my/team/mail/',send_mail,name="my team mail"),
    path('',dashboard,name="dashboard"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
