from django.shortcuts     import render
from django.http          import HttpResponse
from django.http.response import JsonResponse

from api.models       import  User, Meetings
from api.serializers  import  UserSerializer, MeetingsSerializer

from rest_framework            import generics 
from rest_framework.response   import Response
from rest_framework.decorators import api_view

import json

# Create your views here.

# Function based views for more flexibility
@api_view(['POST'])
def Userlogin(request,*args):
    if request.method=='POST':
        try:
            print("\n\n")
            print(request)
            print(request.data['username'])
            try:
                queryset = User.objects.get(username=request.data['username'])
                print(queryset)
                flag = {"login": "true"}
            except:
                print("No data")
                flag = {"login": "false"}

        except:
            return HttpResponse(status=404)
        return Response(flag)

#To retrieve meetings
@api_view(['POST'])
def UserSearch(request,*args):
    if request.method=='POST':
        try:
            data = {
                "username": []
            }
            print("\n\n")
            print(request)
            print(request.data['username'])
            queryset = User.objects.filter(username__contains="{}".format(request.data['username']))
            print(queryset)
            #serializer = UserSerializer(queryset)
            print("\n\n")
            for i in queryset:
                serializer = UserSerializer(i)                
                data['username'].append(serializer.data['username'])

            

            print("\n",data)
            #data2 = json.loads(data)
            #print("\n",data2)
            return JsonResponse(data)
            
            
        except:
            return HttpResponse(status=404)


#Class based views for less code
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MeetingList(generics.ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    
    def retrieve(self, request, username):
    
        queryset = User.objects.get(username=username)
        serializer = UserSerializer(queryset)        
        return Response(serializer.data)

