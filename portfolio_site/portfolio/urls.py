from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('form/', views.form_view, name='form_view'),
    #path('about/', views.about, name='about'),
    #path('projects/', views.projects, name='projects'),
    #path('contact/', views.contact, name='contact'),
]

