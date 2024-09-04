import datetime
from django.shortcuts import render
from odel import renderers


# Create your views here.
def index(request):
    """view for the index or home page"""
    return render(request, "main/index.html", )

def dashboard(request):
    return render(request, 'main-dashboard/dashboard.html')

def dashboard_form_data(request):
    return render(request, 'main-dashboard/forms.html')

def dashboard_fee_payment_data(request):
    return render(request, 'main-dashboard/fee-payment-form.html')

def dashboard_bio_data(request):
    return render(request, 'main-dashboard/bio-data-form.html')

def dashboard_generate_invoice_view(request):
    data = {
        'today': datetime.date.today(), 
        'amount': 15000,
        'customer_name': 'Josiah Livinus',
        'invoice_number': 1233434,
    }
    return render(request, 'main-dashboard/invoice.html', data)

def dashboard_generate_invoice_pdf(self, request, *args, **kwargs):
    data = {
        'today': datetime.date.today(), 
        'amount': 15000,
        'customer_name': 'Josiah Livinus',
        'invoice_number': 1233434,
    }
    return renderers.render_to_pdf('main-dashboard/invoice.html', data)

def dashboard_profile_settings(request):
    return render(request, 'main-dashboard/profile-setting.html')


def dashboard_documents(request):
    return render(request, 'main-dashboard/documents.html')




def about(request):
    """view for the about us page"""
    return render(request, "main/about.html", )

def contact(request):
    """view for the about us page"""
    return render(request, "main/contact.html", )