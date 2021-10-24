from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/add/',                    views.UserRegister         ),
    path('api/login/',                  views.Userlogin            ),
    path('api/list/',                   views.UserSearch           ),
    path('api/profile/<str:username>/', views.UserDetail.as_view() ),
    path('api/meetings/all/',            views.MeetingList.as_view()),
    path('api/meetings/hosted/',         views.MeetingHosted        ),
    path('api/meetings/invited/',        views.MeetingInvited       ),
]

urlpatterns = format_suffix_patterns(urlpatterns)