from django.db import models

class Employees(models.Model):
    ps_no = models.IntegerField(primary_key=True)
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Gender = models.CharField(max_length=6)
    Designation = models.CharField(max_length=50)
    Contact = models.BigIntegerField()
    LTIM_MailID = models.CharField(max_length=50)

class Devices(models.Model):
    assetNo = models.IntegerField(primary_key=True)
    assetType = models.CharField(max_length=50)
    assetBrand = models.CharField(max_length=50)
    assetModel = models.CharField(max_length=50,null=True)
    assetYear = models.CharField(max_length=50,null=True)
    assetOsVersion = models.CharField(max_length=50,null=True)
    assetSerialNumber = models.CharField(max_length=50,null=True) 
    assetUpdate = models.CharField(max_length=50,null=True)
    assetOwnership = models.CharField(max_length=50)
    assetLocation = models.CharField(max_length=50)
    assetAvailability = models.CharField(max_length=50,null=True, default='Available')

class DeviceReport(models.Model):
    ps_no = models.ForeignKey(Employees,on_delete=models.CASCADE)
    assetNo = models.ForeignKey(Devices,on_delete=models.CASCADE)
    dateBorrowed = models.DateTimeField(null=True)
    dateReturned = models.DateTimeField(null= True)
