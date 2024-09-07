import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template, render_to_string
from django.urls import reverse
from xhtml2pdf import pisa
from weasyprint import HTML, CSS

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
    """view to render the admission letter for the user."""
    context = {"user": request.user}
    html_content = render_to_string('main/admission_letter_pdf.html', context)
    pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="admission_letter.pdf"'
    return response


def render_student_info(request, *args, **kwargs):
    context = {"user": request.user}
    html_content = render_to_string('main/student_info_pdf.html', context)
    pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Student_info.pdf"'
    return response


@login_required
def accept_admission(request):
    if request.method == "POST":
        student = Student.objects.get(user=request.user.id)
        student.has_accepted = True
        student.save()
        return redirect('/dashboard')
    return render(request, 'main-dashboard/accept_admission.html')


@login_required
def admission_invoice(request):
    context = {"user": request.user}
    html_content = render_to_string('main/admission_invoice_pdf.html', context)
    pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="admission_invoice.pdf"'
    return response