from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def privacy_policy(request):
    return render(request, "home/privacy_policy.html")
