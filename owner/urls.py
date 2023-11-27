from django.urls import path
from owner.views import *

app_name = 'owner'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_owner'),
    path('list_all_service/', list_all_service, name='list_all_service'),
]