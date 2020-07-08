from django.contrib import admin

from .models import Blog #.models에서 Blog import
# Register your models here.
admin.site.register(Blog)#admin 사이트에 블로그클래스 추가