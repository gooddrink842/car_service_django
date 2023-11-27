from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from technician.models import CarService
from utility.util import check_is_completed

@login_required
def dashboard(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'dashboard_owner.html', context=context)

@login_required
def list_all_service(request):
    context = dict()
    if request.method == 'POST':
        idToRestore = request.POST.get('restore')
        car_service = CarService.objects.get(pk=int(idToRestore))
        car_service.is_deleted = False
        car_service.save()

    if request.user.is_owner:
        car_services = CarService.objects.all()

        rendered_car_services = []
        for car_service in car_services:

            parts_to_service = car_service.part_to_service.all()
            status_now = None
            if check_is_completed(parts_to_service):
                status_now = "Aktif"
            else:
                status_now = "Belum diputuskan"
            if car_service.is_deleted:
                status_now = "Deleted"
            rendered_car_services.append((car_service, car_service.service_date.strftime('%Y-%m-%d'), status_now))
        context['car_services'] = rendered_car_services
        return render(request, 'list_all_service.html', context)
    else:
        return redirect('owner:dashboard_owner')