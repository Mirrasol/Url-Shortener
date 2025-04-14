from api import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('index/', views.URLListView.as_view()),
    path('shorten_url/', views.URLCreateView.as_view()),
]
