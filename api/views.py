from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from api.models       import  User
from api.serializers  import UserSerializer

from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.decorators import api_view


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

#Class based views for less code
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    
    def retrieve(self, request, username):
    
        queryset = User.objects.get(username=username)
        serializer = UserSerializer(queryset)        
        return Response(serializer.data)
        
