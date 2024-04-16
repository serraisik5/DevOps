from django.shortcuts import render, redirect
from .models import Person  

def list_persons(request):
    persons = Person.objects.all()
    return render(request, 'list.html', {'persons': persons})

def delete_person(request, pk):
    if request.method == 'POST':
        person = Person.objects.get(pk=pk)
        person.delete()
        return redirect('list_persons')
    else:
        return redirect('list_persons')
