from django.shortcuts import render 
import random
# from .list import list
from .models import RandomList

# Create your views here.

def home(requset):
    lists = list(RandomList.objects.all())
    lists = random.sample(lists , 1)

    if requset.method == 'POST':
        form = requset.POST
    
  
    return render(requset , 'home.html' , {'lists' : lists} )
#{'lists' : list}