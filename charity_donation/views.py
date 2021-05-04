from django.shortcuts import render, redirect
from django.views import View
from charity_donation.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


class LandingPageView(View):
    def get(self, request):
        return render(request, 'base.html')


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'form.html')


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('main_view')


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_view')
        else:
            return redirect('register_view')


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return redirect('register_view')
        try:
            User.objects.get(username=email)
            return redirect('register_view')
        except:
            try:
                User.objects.get(username=email)
            except:
                User.objects.create_user(name=name,
                                         surname=surname,
                                         email=email,
                                         username=email,
                                         password=password)
                return redirect('login_view')
