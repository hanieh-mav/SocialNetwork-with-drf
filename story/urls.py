from django.urls import path 
from .views import home

app_name = 'story'

urlpatterns = [
    path('',home,name="home")

]
