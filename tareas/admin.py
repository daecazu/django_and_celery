from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .tasks import send_users_emails
class UserAdmin(UserAdmin):


    actions =['send_emails_action',]

    def send_emails_action(self,request,queryset):
        send_users_emails.delay()
        filas_actualizadas=queryset.update(is_staff=True)
        return True

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
