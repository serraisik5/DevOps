from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_persons, name='list_persons'),
    path('delete/<int:pk>/', views.delete_person, name='delete_person'),
]
