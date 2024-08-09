from django.urls import path
from userapp.views import help_template, rules, advertisement, reg

urlpatterns = [
    path('help/', help_template, name='help_template'),
    path('rules/', rules, name='rules'),
    path('advertisement/', advertisement, name='advertisement'),
    path('reg/', reg, name='registration'),
]
