from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visit_time import format_duration
from datacenter.visit_time import get_duration
from datacenter.visit_time import is_visit_long
from django.shortcuts import get_object_or_404

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        visit_duration = get_duration(visit)
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(visit_duration),
            'is_strange': is_visit_long(visit_duration)
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
