from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_header = 'Smart Home'


admin_site = CustomAdminSite()
