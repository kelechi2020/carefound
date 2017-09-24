from django.shortcuts import render

from atiku.models import State, ApplicantInfo


def page(request):
    states = State.objects.all()
    applicant_number = [ApplicantInfo.objects.filter(state=state.name).count() for state in states]
    from pprint import pprint
    pprint(type(applicant_number))
    pprint(type(states))

    return render(request, 'generate.html', {'states':states, 'applicant_number': applicant_number})
