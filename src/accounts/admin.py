from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.site_header = 'Developer Social Network Administration'
admin.site.site_title = 'Welcome To Developer Social Network'
admin.site.index_title = 'Welcome To Developer Social Network'
