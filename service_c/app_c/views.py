from django.shortcuts import render, get_object_or_404, redirect
from service_b.app_b.models import Person  

def list_names(request):
    persons = Person.objects.all()
    return render(request, 'list_names.html', {'persons': persons})

def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('list_names')
