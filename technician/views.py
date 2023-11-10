import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarService, PartToService
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404

@login_required
def dashboard(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'dashboard_technician.html', context=context)

@login_required
def create_service_form(request):
    if request.method == 'POST':
        num_parts = int(request.POST.get('num_parts', 1))  # Ambil jumlah parts yang ingin dibuat, defaultnya 1

        license_plate = request.POST.get('license_plate')
        brand = request.POST.get('brand')
        techinician_name = request.POST.get('staff_service_name')
        techinician_phone = request.POST.get('phone_number')
        service_date = request.POST.get('tanggal')

        car_service = CarService.objects.create(
            user=request.user,
            license_plate=license_plate,
            brand=brand,
            service_date=datetime.datetime.strptime(service_date, '%Y-%m-%d'),
            techinician_name=techinician_name,
            techinician_phone=techinician_phone,
        )

        # Simpan PartToService berdasarkan jumlah yang diinginkan
        for i in range(num_parts):
            part_to_service_text = request.POST.get(f'part_to_service_{i}')
            car_photo = request.FILES.get(f'car_photo_{i}')

            if part_to_service_text:
                part_to_service = PartToService(
                    car_service=car_service,
                    parts_to_service=part_to_service_text,
                    car_photo=car_photo
                )
                part_to_service.save()

        return render(request, 'create_service_form.html', {'status': 'success'})
    else:
        return render(request, 'create_service_form.html')