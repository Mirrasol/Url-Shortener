from django.urls import path
from links import views

urlpatterns = [
    path('shorten_url/', views.create_short_url, name='shorten_url'),
    path('index/', views.get_urls_list, name='urls_list'),
    path('<str:hash>', views.redirect_to_shortened, name='redirect_url'),
#     # path('sign_up/', views.register_user, name='sign_up'),
#     # path('login/', views.login_user, name='login'),
#     # path('logout/', views.logout_user, name='logout'),
]
