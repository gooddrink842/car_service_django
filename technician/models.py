from django.db import models
from authentication.models import UserManage

class CarService(models.Model):
    user = models.ForeignKey(UserManage, on_delete=models.CASCADE, related_name='car_services')
    license_plate = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)
    service_date = models.DateField(auto_now=True)
    techinician_name = models.CharField(max_length=100, default="None")  # Tambahkan field Nama Staff Service
    techinician_phone = models.CharField(max_length=15, default="None")  # Tambahkan field Nomor HP Tukang Service

    def __str__(self):
        return f"{self.user.username}'s Car Service Information"
    
class PartToService(models.Model):
    car_service = models.ForeignKey(CarService, on_delete=models.CASCADE, related_name='part_to_service')

    parts_to_service = models.TextField()
    car_photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return f"PartToService for {self.car_service.user.username}'s Car Service"
