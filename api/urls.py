from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/', views.TestList.as_view()),
    path('api/<int:pk>/', views.TestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)