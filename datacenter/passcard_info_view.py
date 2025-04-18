from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datacenter.models import Passcard, Visit
from datacenter.helpers import format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        entered_at = localtime(visit.entered_at)

        if visit.leaved_at:
            duration = localtime(visit.leaved_at) - entered_at
            leaved_at = localtime(visit.leaved_at)
        else:
            duration = localtime() - entered_at
            leaved_at = 'ещё в хранилище'

        this_passcard_visits.append({
            'entered_at': entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit),
            'leaved_at': leaved_at
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)