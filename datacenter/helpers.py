from django.utils.timezone import localtime


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours}:{minutes:02}"


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is None:
        duration = localtime() - localtime(visit.entered_at)
    else:
        duration = localtime(visit.leaved_at) - localtime(visit.entered_at)
    return duration.total_seconds() > minutes * 60