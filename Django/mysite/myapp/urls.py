from django.urls import path

from myapp import views


urlpattens=[
    path('',views.index,name='index')
]