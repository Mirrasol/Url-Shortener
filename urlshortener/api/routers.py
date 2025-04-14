from api import views
from django.urls import path

# from rest_framework import routers

# router = routers.DefaultRouter()

urlpatterns = [
    path('urls/index/', views.URLListView.as_view()),
    path('urls/shorten_url/', views.URLCreateView.as_view()),
    path('users/', views.UsersListView.as_view()),
]
