from django.contrib import admin
from .models import User, Meetings

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','college','year','degree','country','about')

class MeetingsAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'start_time','end_time','host',"host_name","host_email",'participant_2',"participant_2_name","participant_2_email",'participant_3',"participant_3_name","participant_3_email",'participant_4',"participant_4_name","participant_4_email")
    #list_display = ('room_name', 'start_time','end_time','participant_1','participant_2','participant_3','participant_4')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Meetings,MeetingsAdmin)
