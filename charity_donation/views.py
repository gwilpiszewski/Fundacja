from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User


# Create your views here.

class LandingPageView(View):
    def get(self, request):
        return render(request, 'base.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    # def post(self, request):
    # first_name = request.POST.get('name')
    # last_name = request.POST.get('surname')
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # password2 = request.POST.get('password2')
    #
    # if first_name and last_name and email and password and password2 !="" and '@' in email and password == password2:
    #     User.objects.create(first_name=first_name,
    #                         last_name=last_name,
    #                         email=email,
    #                         password=password)
    #     return
