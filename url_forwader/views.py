from django.shortcuts import redirect
from .models import Urls

def redirect_view(request):
    response = redirect(Urls.objects.filter(id=1)[0].url)
    return response