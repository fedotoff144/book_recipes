from django.urls import path
from userapp.views import help_template, rules, advertisement, reg, login_view, logout_view

app_name = 'userapp'

urlpatterns = [
    path('help/', help_template, name='help_template'),
    path('rules/', rules, name='rules'),
    path('advertisement/', advertisement, name='advertisement'),
    path('reg/', reg, name='registration'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]
