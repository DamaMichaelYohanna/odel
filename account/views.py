from django.contrib import messages
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect

from account.models import CustomUser


def register_one(request):
    if request.method == 'POST':
        entry_mode = request.POST.get("entry_mode")
        email = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm-password")
        if password1 != password2:
            messages.error(request, "Password Mismatch!")
            return render(request, 'main/registration_form.html')
        try:
            user = CustomUser.objects.create(email=email)
            user.set_password(password1)
            messages.success(request, "Account created Sucessfully.")
            return redirect("/application")
        except IntegrityError:
            messages.error(request, "Email address already used!")
            return render(request, 'main/registration_form.html')


    else:
        return render(request, 'main/registration_form.html')
