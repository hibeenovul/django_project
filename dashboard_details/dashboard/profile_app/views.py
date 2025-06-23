from django.shortcuts import render, redirect
from .models import UserProfile 
from .forms import UserProfileForm

def profile(request):
    
    latest_profile = UserProfile.objects.last()  # Load the latest profile entry
    
    # check if form is submitted
    # and handle the form submission
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=latest_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Assuming you have a URL named 'profile' to redirect to after saving
        
        else:
            print("Form errors:", form.errors)  # 👈 See why it fails
            
    else:
        form = UserProfileForm(instance=latest_profile)  # Load the form with the latest profile data
    
    latest_profile = UserProfile.objects.last()  # Get the latest profile entry
    
    return render(request, 'profile_app/profile.html', {
        'form': form,
        'profile': latest_profile
    })
    
    
    
    
    
# Create your views here.


 