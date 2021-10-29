from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/users',                   views.Users                ),  # GET  -To get all users list
    path('api/add/',                    views.UserRegister         ),  # POST -Register
    path('api/login/',                  views.Userlogin            ),  # POST -Login 
    path('api/list/',                   views.UserSearch           ),  # POST -Search users while creating room
    path('api/profile/<str:username>/', views.UserDetail.as_view() ),  # GET  -To get details of user

    path('api/meetings/set/',           views.MeetingSet           ),  # POST -To set a meeting 
    path('api/meetings/total/',         views.MeetingAll           ),  # POST -To get user    meetings
    path('api/meetings/hosted/',        views.MeetingHosted        ),  # POST -To get hosted  meetings
    path('api/meetings/invited/',       views.MeetingInvited       ),  # POST -To get invited meetings
    path('api/meetings/all/',           views.MeetingList.as_view()),  # POST -To get all     meetings
]

urlpatterns = format_suffix_patterns(urlpatterns)