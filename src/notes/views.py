from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect


def home_page_redirect(request: HttpRequest) -> HttpResponse:
    return redirect('api/v1/', permanent=True)
