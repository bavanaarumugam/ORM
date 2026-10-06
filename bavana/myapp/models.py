from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    vehicle_name=models.CharField(max_length=10)
    vehicle_ID=models.AutoField
    Brand=models.CharField(max_length=10)
    Colour=models.CharField(max_length=10)
    Year=models.IntegerField()
    Price=models.DecimalField()
    Model_name=models.CharField(max_length=10)

class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["vehicle_name","vehicle_ID","Brand","Colour","Year","Price","Model_name"]


