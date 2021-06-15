from django.shortcuts import render
import redis 

# Create your views here.

def home(request):
    return render(request,'story/story_list.html')