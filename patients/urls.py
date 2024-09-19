
from django.urls import path
from.views import *

urlpatterns = [
    
    path('homepage/', home),
    path('aboutpage/', about),
    path('p_loginpage/', patientlogin),
    path('d_loginpage/',doctorlogin),
    path('dlogout/', logoutview),
    path('addpage/', addpatient)


]
