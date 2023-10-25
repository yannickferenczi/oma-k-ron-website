from django.shortcuts import render


def index(request):
    """ This function renders the home page """
    return render(request, 'home/index.html')


def privacy_policy(request):
    """ This function renders the privacy policy page """
    return render(request, "home/privacy_policy.html")
