from django.contrib import admin

# Register your models here.
from access_token.models import AccessToken,UserKeys
# Register your models here.


class AccessTokenAdmin(admin.ModelAdmin):
    list_display=('token','description','name')
 
admin.site.register(AccessToken,AccessTokenAdmin)
admin.site.register(UserKeys)