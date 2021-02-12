from django.urls import path,include
from .views import kamana

urlpatterns =[
    path('',kamana,name="kamana")
]