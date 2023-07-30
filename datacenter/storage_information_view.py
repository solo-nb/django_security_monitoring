from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visit_time import get_duration
from datacenter.visit_time import format_duration
from datacenter.visit_time import is_visit_long

def storage_information_view(request):
    
    non_closed_visits = []
    for person_not_leaved in Visit.objects.filter(leaved_at=None): 
        visit_duration = get_duration(person_not_leaved)
        non_closed_visits.append(
            {
                'who_entered': person_not_leaved.passcard,
                'entered_at': person_not_leaved.entered_at,
                'duration': format_duration(visit_duration),
                'is_strange': is_visit_long(visit_duration)
            }
        )
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
