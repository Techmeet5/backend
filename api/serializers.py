from .models import User, Meetings, MeetingDetails
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','college','year','degree','country','about']
        

class MeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = ['room_name', 'start_time','end_time','host',"host_name","host_email",'participant_2',"participant_2_name","participant_2_email",'participant_3',"participant_3_name","participant_3_email",'participant_4',"participant_4_name","participant_4_email"]
        #fields = ['room_name', 'start_time','end_time','participant_1','participant_2','participant_3','participant_4']
