from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/add/',                    views.UserList.as_view()   ),
    path('api/login/',                  views.Userlogin            ),
    path('api/list/',                   views.UserSearch           ),
    path('api/profile/<str:username>/', views.UserDetail.as_view() ),
    path('api/meetings/',               views.MeetingList.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)