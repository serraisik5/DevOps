from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person, created = Person.objects.get_or_create(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
            if created:
                return redirect('success')
            else:
                return render(request, 'name_exists.html')
    else:
        form = PersonForm()

    return render(request, 'person.html', {'form': form})

def success(request):
    total_records = Person.objects.count()
    return render(request, 'success.html', {'total_records': total_records})
