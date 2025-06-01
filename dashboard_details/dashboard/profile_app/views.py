from django.shortcuts import render
from .forms import UserProfileForm

def profile(request):
    form = UserProfileForm
    return render(request, 'profile_app/profile.html', {'form': form})

# Create your views here.
