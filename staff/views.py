from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from technician.models import CarService, PartToService
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail

# static variable
WEBSITE = "https://web-production-d8f5.up.railway.app/"

@login_required
def dashboard(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'dashboard_staff.html', context=context)

@login_required
def service_approval_list(request):
    if request.user.is_staff_member:
        car_services = CarService.objects.all()

        for car_service in car_services:
            parts_to_service = car_service.part_to_service.all()

        context = {'car_services': car_services}
        return render(request, 'service_approval_list.html', context)
    else:
        return redirect('/staff/dashboard')

############ UTIL ############
def check_is_completed(parts_to_service):
    is_not_completed = False
    for part_to_service in parts_to_service:
        if (not part_to_service.is_approved) and (not part_to_service.is_rejected):
            is_not_completed = True
    return not is_not_completed
##############################

def service_detail(request, service_id):
    car_service = CarService.objects.get(pk=service_id)

    parts_to_service = car_service.part_to_service.all()
    status_complete_before_post = check_is_completed(parts_to_service)

    if request.method == 'POST':
        car_service_id = request.POST.get('car_service_id')
        part_to_service_id = request.POST.get('part_to_service_id')
        action = request.POST.get('action')

        if action == 'approve':
            part_to_service = PartToService.objects.get(pk=part_to_service_id)
            part_to_service.is_approved = True
            part_to_service.save()
        elif action == 'reject':
            part_to_service = PartToService.objects.get(pk=part_to_service_id)
            part_to_service.is_rejected = True
            part_to_service.save()

        car_service = CarService.objects.get(pk=car_service_id)
    
    parts_to_service = car_service.part_to_service.all()
    is_completed = check_is_completed(parts_to_service)

    if (not status_complete_before_post) and (is_completed):
        print(send_mail(
            f"Pesanan Service Mobil Baru ke-{service_id}",
            f"Haloo, Terdapat Pesanan Service Mobil yang telah diputuskan\n\nBerikut merupakan linknya: {WEBSITE}staff/generate_pdf/{service_id}/\n\n",
            f"{settings.EMAIL_HOST_USER}",
            recipient_list=["Rickyprawiro@yahoo.com"],
            fail_silently=False,
        ))

    no_wa_temp = car_service.techinician_phone.strip()
    if no_wa_temp.startswith("0"):
        no_wa_temp = "62" + no_wa_temp[1:]
    whatsapp_link = f'https://api.whatsapp.com/send?phone={no_wa_temp}&text=Haloo%2C%20Terdapat%20Pesanan%20Service%20Mobil%20yang%20telah%20diputuskan%0A%0ABerikut%20merupakan%20linknya%3A%20{WEBSITE}staff/generate_pdf/{service_id}%2F%0A%0A'
    
    context = {'car_service': car_service, 'parts_to_service_list':parts_to_service, 'is_completed':is_completed, 'whatsapp_link':whatsapp_link}
    return render(request, 'service_detail.html', context)

def generate_pdf(request, car_service_id):
    car_service = get_object_or_404(CarService, id=car_service_id)
    parts_to_service = car_service.part_to_service.all()

    template_path = 'html2pdf.html'
    context = {'car_service': car_service, 'parts_to_service_list':parts_to_service}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="car_service_{car_service.id}.pdf'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', content_type='text/plain')
    return response