from django.utils.timezone import localtime


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours}:{minutes:02}"


def is_visit_long(visit, minutes=60):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime()
    duration = leaved_at - entered_at
    return duration.total_seconds() > minutes * 60