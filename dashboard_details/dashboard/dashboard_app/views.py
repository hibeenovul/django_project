from django.shortcuts import render
from profile_app.models import UserProfile

def dashboard(request):
    profile = UserProfile.objects.last()
    return render(request, 'dashboard_app/dashboard.html',{
        'profile' : profile
    })

# Create your views here.