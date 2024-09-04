from django.contrib import messages
from django.contrib.auth import authenticate
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


def student_login (request):
    if request.method == 'POST':
        student_id = request.POST.get("student_id")
        password = request.POST.get("password")
        if not student_id or not password:
            messages.error(request, "Fields can't be empty!")
            return render(request, 'main/login_form.html')
        try:
            print("trying here")
            user = authenticate(request, username=student_id, password=password)
            if not user:
                messages.error(request, "Invalid Credentials!")
                return render(request, 'main/login_form.html')

            if user.student.mat_number and student_id != user.student.mat_number:
                messages.error(request, f"Use {user.student.mat_number} as your matric number")
                return render(request, 'main/login_form.html')
            # user.set_password(password1)
            messages.success(request, "Login Sucessfully.")
            return redirect("/dashboard")
        except IntegrityError:
            messages.error(request, "Email address already used!")
            return render(request, 'main/login_form.html')


    else:
        return render(request, 'main/login_form.html')