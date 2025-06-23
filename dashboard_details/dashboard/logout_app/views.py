from django.shortcuts import render, redirect
from profile_app.models import UserProfile

def logout(request):
    # Assuming you want to clear the session or perform logout logic
    
    UserProfile.objects.all().delete()  # Clear all user profiles (if needed)
    
    request.session.flush()  # Clear the session data
    
    return redirect('dashboard')
   # return render(request, 'logout_app/logout.html', {
   #     'message': 'You have been logged out successfully.'
   # })
# Create your views here.
