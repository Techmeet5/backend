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
                print("check")
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
            data = []
            
            print("\n\n")
            print(request)
            print("dcds")
            print(request.data['username'])
            print("ese")
            queryset = User.objects.filter(username__contains="{}".format(request.data['username']))
            print(queryset)
            #serializer = UserSerializer(queryset)
            print("\n\n")
            for i in queryset:
                value = {
                    "username"  :"",
                    "name"      :"",
                    "email"     :""
                }
                serializer = UserSerializer(i)
                print("\n\n\n\n\n ----------------------------------------------------------")
                print(serializer.data)
                print(serializer.data['first_name'])
                print(serializer.data['email'])
                print("value dict before -",value)            
                value["username"]   = serializer.data['username']
                value["name"]       = serializer.data['first_name']
                value["email"]      = serializer.data['email'] 
                print("value dict after -",value)            
                data.append(value)
                print(data)
            

            print("\n",data)
            #data = json.loads(data)
            #print("\n",data)
            return Response(data)
            
            
        except:
            print("NOT")
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

