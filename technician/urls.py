from django.urls import path
from technician.views import *

app_name = 'technician'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_technician'),
    path('create_service_form/',create_service_form, name='create_service_form'),
]