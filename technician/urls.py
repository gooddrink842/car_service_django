from django.urls import path
from technician.views import *

app_name = 'technician'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_technician'),
    path('create_service_form/',create_service_form, name='create_service_form'),
    path('list_for_edit/',list_for_edit, name='list_for_edit'),
    path('edit_service/<int:service_id>/', edit_service, name='edit_service'),
    path('history_service/', history_service, name='history_service'),
]