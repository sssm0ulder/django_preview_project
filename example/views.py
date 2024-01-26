from django.shortcuts import render
from .models import Person
from .utils import add_fake_data_to_database


def person_list(request):
    persons = Person.objects.all()

    if len(persons) == 0:
        add_fake_data_to_database()

    return render(request, 'person_list.html', {'persons': persons[:5]})
