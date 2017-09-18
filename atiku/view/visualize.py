from django.shortcuts import render

def page(request):
    return render(request, 'home v3.html')