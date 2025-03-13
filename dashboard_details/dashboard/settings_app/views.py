from django.shortcuts import render

def settings(request):
    return render(request, 'settings_app/settings.html')

# Create your views here.
