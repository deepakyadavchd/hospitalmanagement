
from django.urls import path
from.views import *

urlpatterns = [
    
    path('homepage/', home),
    path('aboutpage/', about),
    path('p_loginpage/', patientlogin),
    path('d_loginpage/',drlogin),
    path('dlogout/', logoutview),
    path('plogout/', poutview),
    path('addpage/', addpatient), 
    path('history/', htr)


]
