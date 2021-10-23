from django.contrib import admin
from .models import User, Meetings

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','college','year','degree','country','about')

class MeetingsAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'start_time','end_time','host','participant_2','participant_3','participant_4')
    
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Meetings,MeetingsAdmin)
