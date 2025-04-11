from django.urls import path
from links import views

urlpatterns = [
    path('sign_up/', views.register_user, name='sign_up'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
]
