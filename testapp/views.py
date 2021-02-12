from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def kamana(request):
    return render(request,'testapp\kamana.html')