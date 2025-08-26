from django.urls import path
from applicants import views


app_name = "applicants"
urlpatterns = [
    path('registration', views.applicant_register, name='registration'),
    path('login', views.applicant_login, name='login'),
    # path("applicant/apply", views.applicant_apply, name="applicant_apply"),
    path("dashboard", views.applicant_dashboard, name="applicant_dashboard"),
    path("slip/download", views.applicant_dashboard, name="download_slip"),

]