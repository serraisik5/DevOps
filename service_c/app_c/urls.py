from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_names, name='list_names'),
    path('delete/<int:pk>/', views.delete_person, name='delete_person'),
]
