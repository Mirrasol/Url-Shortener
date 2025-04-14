from django.urls import path
from links import views

urlpatterns = [
    path('shorten_url/', views.create_short_url, name='shorten_url'),
    path('index/', views.get_urls_list, name='urls_list'),
    path('<str:hash>', views.redirect_to_shortened, name='redirect_url'),
]
