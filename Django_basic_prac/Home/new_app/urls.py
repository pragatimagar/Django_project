from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='new_app'),
    path('brands',views.brands,name='brands'),
    path('categories',views.categories,name='categories'),
    path('contact',views.contact,name='contact')
]