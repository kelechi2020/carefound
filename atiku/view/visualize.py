from django.shortcuts import render

from atiku.models import State


def page(request):
    states = State.objects.all()

    return render(request, 'home v3.html', {'states':states})
