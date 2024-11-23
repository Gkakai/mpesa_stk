from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('myApp/', views.home, name='thank_you'),
    path('stk_push/', views.stk_push, name='stk_push'),
    path('thank_you', views.thank_you, name='thanks')
]
   