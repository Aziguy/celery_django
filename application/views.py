from django.http import HttpResponse
from django.shortcuts import render
from .tasks import make_some_iteration


# Create your views here.
def make_some_iteration_view(request):
    make_some_iteration.delay()
    return HttpResponse("Done!")
