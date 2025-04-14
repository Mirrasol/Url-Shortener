from django.urls import path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path('index/', views.URLListView.as_view()),
    path('shorten_url/', views.URLCreateView.as_view()),
]
