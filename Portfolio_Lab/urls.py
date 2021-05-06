"""Portfolio_Lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from charity_donation.views import AddDonationView, LandingPageView, RegisterView, LogOutView, CreateInstitutionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='main_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogOutView.as_view(), name='logout_view'),
    path('register/', RegisterView.as_view(), name='register_view'),
    path('create_institution/', CreateInstitutionView.as_view(), name='create_institution_view'),
    path('add_donation/', AddDonationView.as_view(), name='add_donation_view')

]
