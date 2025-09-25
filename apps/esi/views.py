# Create your views here.
import logging

from django.http import HttpRequest
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def sso_redirect(request: HttpRequest) -> HttpResponse:
    pass


def recieve_callback(request: HttpRequest) -> HttpResponse:
    pass
