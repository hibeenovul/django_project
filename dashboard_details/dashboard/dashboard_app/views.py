from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard_app/dashboard.html')

# Create your views here.
