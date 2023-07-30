from datacenter.models import Visit
from django.utils import timezone


def get_duration(visit: Visit) -> int:
    if not Visit.leaved_at:
        return int((timezone.localtime() 
                    - Visit.entered_at).total_seconds())
    return int((Visit.leaved_at 
                - Visit.entered_at).total_seconds())


def format_duration(total_seconds: int) -> str:
    return '{}:{:02}'.format(
        total_seconds//3600,
        total_seconds%3600//60
    )


def is_visit_long(total_seconds: int) -> bool:
    return total_seconds > 3600
