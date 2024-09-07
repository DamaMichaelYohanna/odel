from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('dashboard', views.dashboard, name='dashboard_page'),
    path('form', views.dashboard_form_data, name='dashboard_form'),
    path('fee', views.dashboard_fee_payment_data, name='fee_payment_form'),
    path('biodata', views.dashboard_bio_data, name='bio-data_form'),
    path('accept-admission', views.accept_admission, name='accept-admission'),
    path('admission-invoice', views.admission_invoice, name='admission_invoice'),
    path('invoice', views.dashboard_generate_invoice_view, name='invoice_page'),
    path('invoices', views.dashboard_generate_invoice_pdf, name='invoices_form'),
    path('profile', views.dashboard_profile_settings, name='profile_setting_page'),
    path('document', views.dashboard_documents, name='documents_page'),
    path('payment', views.dashboard_payments, name='payments_page'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='contact-page'),
    path('admission-download', views.render_admission, name='admission_letter'),
    path('gen-invoice', views.render_pdf, name='render pdf'),
]
