from django.http import HttpRequest
from django.http import HttpResponse


def current_status(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Current status')
