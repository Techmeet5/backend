from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts     import render
from django.http          import HttpResponse
from django.http.response import JsonResponse

from api.models       import  User, Meetings
from api.serializers  import  UserSerializer, MeetingsSerializer

from rest_framework            import generics, serializers
from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.parsers    import JSONParser


#from backend.api import serializers

# Create your views here.

# To get Users
@api_view(['GET'])
def Users(request,*args):
    if request.method == 'GET':
        queryset   = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse(serializer.data,  safe=False)

# To Register  
@api_view(['POST'])
def UserRegister(request,*args):
    if request.method=='POST':
        try:
            user = request.data['username']
            if User.objects.filter(username=user).exists():
                return Response("Username already exists")
            else:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=201)

        except:
            return HttpResponse(status=404)

# To Login
@api_view(['POST'])
def Userlogin(request,*args):
    if request.method=='POST':
        try:
            # In whatever situation json response should be given.. that is why double try block
            try:
                queryset   = User.objects.get(username=request.data['username'])
                serializer = UserSerializer(queryset)
                flag = {"login": "true", "details":serializer.data}
            except:
                flag = {"login": "false"}

        except:
            return HttpResponse(status=404)
        return Response(flag)

#To Search users while creating room
@api_view(['POST'])
def UserSearch(request,*args):
    if request.method=='POST':
        try:
            data = []
            queryset = User.objects.filter(username__contains="{}".format(request.data['username']))
            for i in queryset:
                value = {
                    "username"  :"",
                    "name"      :"",
                    "email"     :""
                }
                serializer = UserSerializer(i)           
                value["username"]   = serializer.data['username']
                value["name"]       = serializer.data['first_name']
                value["email"]      = serializer.data['email'] 
                data.append(value)
            return Response(data)
            
        except:
            return HttpResponse(status=404)















#To set meeting
@api_view(['POST'])
def MeetingSet(request,*args):
    if request.method=='POST':
        try:
            meeting = request.data
            users   = request.data['persons']

            server_meeting = {
            "room_name"      : "","start_time"         : "","end_time"           : "","meet_url"    :"","board_url"     :"",
            "host"           : "","host_name"          : "","host_email"         : "",
            "participant_2"  : "none", "participant_2_name": "none", "participant_2_email": "none@gmail.com",
            "participant_3"  : "none", "participant_3_name": "none", "participant_3_email": "none@gmail.com",
            "participant_4"  : "none", "participant_4_name": "none", "participant_4_email": "none@gmail.com",
            }

            try:
                server_meeting['room_name']  = meeting['name']
                server_meeting['start_time'] = meeting['start']
                server_meeting['end_time']   = meeting['end']
                server_meeting['meet_url']   = meeting['meet_url']
                server_meeting['board_url']  = meeting['board_url']
                
                server_meeting['host']       = users[0]['username']
                server_meeting['host_name']  = users[0]['name']
                server_meeting['host_email'] = users[0]['email']

                server_meeting['participant_2']       = users[1]['username']
                server_meeting['participant_2_name']  = users[1]['name']
                server_meeting['participant_2_email'] = users[1]['email']

                server_meeting['participant_3']       = users[2]['username']
                server_meeting['participant_3_name']  = users[2]['name']
                server_meeting['participant_3_email'] = users[2]['email']

                server_meeting['participant_4']       = users[3]['username']
                server_meeting['participant_4_name']  = users[3]['name']
                server_meeting['participant_4_email'] = users[3]['email']

            except:    
                serializer = MeetingsSerializer(data=server_meeting)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            
            return HttpResponse("Not Valid")
                    
        except:
            return HttpResponse(status=404)








#To retrieve All meetings
@api_view(['POST'])
def MeetingAll(request,*args):
    if request.method=='POST':
        try:
            data = []
            queryset_1= Meetings.objects.filter(host__exact="{}".format(request.data['username']))
            queryset_2 = Meetings.objects.filter(participant_2__exact="{}".format(request.data['username']))
            queryset_3 = Meetings.objects.filter(participant_3__exact="{}".format(request.data['username']))
            queryset_4 = Meetings.objects.filter(participant_4__exact="{}".format(request.data['username']))

            queryset = queryset_4 |  queryset_3 | queryset_2 | queryset_1
                        
            #serializer = UserSerializer(queryset)
            for i in queryset:
                serializer = MeetingsSerializer(i)
                data.append(serializer.data)
            return Response(data)
                    
        except:
            return HttpResponse(status=404)


#To retrieve Hosted meetings
@api_view(['POST'])
def MeetingHosted(request,*args):
    if request.method=='POST':
        try:
            data = []
            queryset = Meetings.objects.filter(host__exact="{}".format(request.data['username']))
            for i in queryset:
                serializer = MeetingsSerializer(i)
                data.append(serializer.data)
            return Response(data)
    
        except:
            print("NOT")
            return HttpResponse(status=404)





#To retrieve Invited meetings
@api_view(['POST'])
def MeetingInvited(request,*args):
    if request.method=='POST':
        try:
            data = []
            queryset_1 = Meetings.objects.filter(participant_2__exact="{}".format(request.data['username']))
            queryset_2 = Meetings.objects.filter(participant_3__exact="{}".format(request.data['username']))
            queryset_3 = Meetings.objects.filter(participant_4__exact="{}".format(request.data['username']))

            queryset = queryset_3 | queryset_2 | queryset_1
                        
            #serializer = UserSerializer(queryset)
            for i in queryset:
                serializer = MeetingsSerializer(i)
                data.append(serializer.data)
            return Response(data)
                    
        except:
            return HttpResponse(status=404)









#Class based views for less code    

class MeetingList(generics.ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    serializer_class = UserSerializer
    #queryset   = User.objects.all()
         
    def retrieve(self, request, username):
        queryset   = User.objects.get(username=username)
        serializer = UserSerializer(queryset)        
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        queryset   = User.objects.get(username=kwargs['username'])

        data = JSONParser().parse(request)        
        User.objects.filter(pk=kwargs['username']).update(**data)
        print(queryset)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
