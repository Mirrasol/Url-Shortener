from api import views
from django.urls import path

# from rest_framework import routers

# router = routers.DefaultRouter()

urlpatterns = [
    path('urls/index/', views.URLListView.as_view(), name='api_urls_list'),
    path('urls/shorten_url/', views.URLCreateView.as_view(), name='api_shorten_url'),
    path('users/', views.UsersListView.as_view(), name='api_users_list'),
]
