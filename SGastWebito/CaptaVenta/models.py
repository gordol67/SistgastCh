from django.db import models


# Create your models here.

class Venta(models.Model):
    codprod = models.CharField(primary_key=True,max_length=13,unique=True,blank=False)
    cantvend = models.DecimalField(max_digits=8, decimal_places=2)
    precventa = models.DecimalField(max_digits=10, decimal_places=2)
    fechventa = models.DateField(null=False)
    codarea = models.CharField(max_length=2,unique=False)


class UM(models.Model):
         codum = models.CharField(primary_key=True,max_length=50,unique=True,blank=False)
         descum = models.CharField(max_length=50,unique=True,blank=False)

class Familia(models.Model):
     codfamilia = models.CharField(primary_key=True,max_length=8,unique=True,blank=False)
     desfami = models.CharField(max_length=30,unique=True,blank=False)


class Areas(models.Model):
    codarea = models.CharField(primary_key=True,max_length=2,unique=True,blank=False)
    desarea = models.CharField(max_length=30,unique=True,blank=False)
    tipoarea = models.CharField(max_length=2,blank=False)
    activa = models.BooleanField()
    codent = models.CharField(max_length=3, unique=True, blank=False)
    area = models.OneToOneField(Venta, on_delete=models.CASCADE,null=False)

class Producto(models.Model):
     codprod = models.CharField(primary_key=True,max_length=13,unique=True,blank=False)
     desprod = models.CharField(max_length=50,unique=True,blank=False)
     costo = models.DecimalField(max_digits=10, decimal_places=4)
     precventa = models.DecimalField(max_digits=10, decimal_places=4)
     codum = models.CharField(max_length=50,unique=True,blank=False)
     codfamilia = models.CharField(max_length=8,unique=True,blank=False)
     um = models.ForeignKey(UM,on_delete=models.CASCADE,null=False)
     familia = models.ForeignKey(Familia,on_delete=models.CASCADE,null=False)
     area = models.ManyToManyField(Areas)
                                

