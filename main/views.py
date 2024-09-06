import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
from xhtml2pdf import pisa

from account.models import Student
from odel import renderers


# Create your views here.
def index(request):
    """view for the index or home page"""
    return render(request, "main/index.html", )


@login_required
def dashboard(request):
    return render(request, 'main-dashboard/dashboard.html')


@login_required
def dashboard_form_data(request):
    return render(request, 'main-dashboard/forms.html')


@login_required
def dashboard_fee_payment_data(request):
    return render(request, 'main-dashboard/fee-payment-form.html')


@login_required
def dashboard_bio_data(request):
    if request.method == "POST":
        pob = request.POST.get("pob")
        dob = request.POST.get("dob")
        marital_status = request.POST.get("marital_status")
        country = request.POST.get("country")
        lga = request.POST.get("lga")
        state = request.POST.get("state")
        contact_address = request.POST.get("contact_address")
        contact_country = request.POST.get("contact_country")
        contact_state = request.POST.get("contact_state")
        contact_lga = request.POST.get("contact_lga")
        nokn = request.POST.get("nokn")
        nokp = request.POST.get("nokp")
        noka = request.POST.get("noka")
        # get the current student profile from user
        relationship = request.POST.get("relationship")
        student_object = Student.objects.get(user=request.user.id)
        student_object.place_of_birth = pob
        student_object.date_of_birth = dob
        student_object.marital_status = marital_status
        student_object.country = country
        student_object.state = state
        student_object.lga = lga
        student_object.contact_country = contact_country
        student_object.contact_state = contact_state
        student_object.contact_lga = contact_lga
        student_object.contact_address = contact_address
        student_object.kin_name =nokn
        student_object.kin_address =noka
        student_object.kin_phone =nokp
        student_object.kin_relation =relationship
        student_object.save()
        return redirect("/dashboard")
        # print(pob, dob, marital_status, state,country, contact_state,contact_address,
        #       contact_lga)
        # print(contact_country, nokn, nokp, noka,relationship)
    else:
        pass
    return render(request, 'main-dashboard/bio-data-form.html')


@login_required
def dashboard_generate_invoice_view(request):
    data = {
        'today': datetime.date.today(),
        'amount': 15000,
        'customer_name': 'Josiah Livinus',
        'invoice_number': 1233434,
    }
    return render(request, 'main-dashboard/invoice.html', data)


@login_required
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


def dashboard_payments(request):
    return render(request, 'main-dashboard/payment.html')


def about(request):
    """view for the about us page"""
    return render(request, "main/about.html", )


def contact(request):
    """view for the about us page"""
    return render(request, "main/contact.html", )


def render_admission(request):
    """view for the about us page"""
    return render(request, "main/admission.html", )


def render_pdf(request, *args, **kwargs):
    template_path = 'main/invoice.html'
    static_file_name = '/static/main/img/about.jpg'
    absolute_path = request.build_absolute_uri(static_file_name)
    context = {'myvar': 'this is your template context', 'u': absolute_path}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    print(request.META)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required
def accept_admission(request):
    if request.method == "POST":
        student = Student.objects.get(user=request.user.id)
        student.has_accepted = True
        student.save()
        return redirect('/dashboard')
    return render(request, 'main-dashboard/accept_admission.html')