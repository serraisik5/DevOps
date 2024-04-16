from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_person, name='person'),
    path('add/', views.add_person, name='person'),
    path('success/', views.success, name='success'),
]
