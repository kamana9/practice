from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    people=Person.objects.all()
    context={
        'people':people
    }
    return render(request,"myapp/index.html",context)