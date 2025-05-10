from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from helpers import format_duration


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in active_visits:
        entered_at = localtime(visit.entered_at)
        duration = localtime() - entered_at

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
