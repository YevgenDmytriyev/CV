from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('work/', views.work, name='work'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

