from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from userapp.views import (help_template,
                           rules,
                           advertisement,
                           register_view,
                           login_view,
                           logout_view,
                           profile,
                           )

app_name = 'userapp'

urlpatterns = [
    path('help/', help_template, name='help_template'),
    path('rules/', rules, name='rules'),
    path('advertisement/', advertisement, name='advertisement'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]
