from django.urls import path
from .views import *
app_name = 'shop'
urlpatterns = [
    path('login/',login , name = 'login'),
    path('register/',Register , name = 'register'),
    path('logout/',logout , name = 'logout'),

]