from django.urls import path

from links import views

urlpatterns = [
    path('sign_up/', views.register_user, name='sign_up'),
]
