from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','college','year','degree','country','about')


# Register your models here.
admin.site.register(User, UserAdmin)