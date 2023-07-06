from django.urls import path
from .views import *
app_name = 'shop'
urlpatterns = [
    path('login/',Login , name = 'login'),
    path('register/',Register , name = 'register'),
    path('logout/',Logout_view , name = 'logout'),
    path('home/',Home , name = 'home'),
    path('service/',createService , name = 'service'),

]