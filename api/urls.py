from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [

    path('api/login/',          views.Userlogin),
    path('api/add/',            views.UserList.as_view()),
    path('api/profile/<str:username>/', views.UserDetail.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)