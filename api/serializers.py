from .models import User, Meetings, MeetingDetails
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','college','year','degree','country','about']
        

class MeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = ['room_name', 'start_time','end_time','host','participant_2','participant_3','participant_4']

