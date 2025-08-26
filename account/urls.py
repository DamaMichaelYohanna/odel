from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = "account"
urlpatterns = [
    # Request reset link
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='account/password_reset.html',
            success_url=reverse_lazy('account:password_reset_done'),
            email_template_name='account/password_reset_email.html',

        ),
        name='password_reset',
    ),
    
    # Email sent confirmation
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html',
           
        ),
        name='password_reset_done',
    ),
    
    # Link clicked → change password
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.html',
             success_url=reverse_lazy('account:password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),
    
    # Password reset complete
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
