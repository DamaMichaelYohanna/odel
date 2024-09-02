from django.shortcuts import render


# Create your views here.
def index(request):
    """view for the index or home page"""
    return render(request, "main/index.html", )

def dashboard(request):
    return render(request, 'main-dashboard/dashboard.html')

def dashboard_form_data(request):
    return render(request, 'main-dashboard/forms.html')

def about(request):
    """view for the about us page"""
    return render(request, "main/about.html", )

def contact(request):
    """view for the about us page"""
    return render(request, "main/contact.html", )