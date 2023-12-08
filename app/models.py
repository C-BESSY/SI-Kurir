from django.db import models


# Create your models here.
    
class Admin(models.Model):
    userid = models.CharField(max_length=8, unique=True,null=True)
    username = models.CharField(max_length=10,null=True)
    password = models.CharField(max_length=10,null=True)

    # def __str__(self):
    #     return self.nama_admin
    
class Barang(models.Model):
    STATUS_CHOICES = (
        ('POS', 'Gagal Dikirim'),   
        ('POD', 'Sukses Dikirim')
    )
    
    id_barang = models.CharField(max_length=12, unique=True)
    nama_pemesan = models.CharField(max_length=50, null=True)
    status_barang = models.CharField(max_length=3, choices=STATUS_CHOICES, default='POD')
    nama_penerima = models.CharField(max_length=50)
    tujuan = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.id_barang
    
class Kurir(models.Model):
    id_kurir = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=50)
    ttl = models.DateField
    no_telepon = models.CharField(max_length=12)
    area_pengiriman = models.CharField(null=True, max_length=150)

    def __str__(self):
        return self.nama

class TaskDelivery(models.Model):
    id_task = models.CharField(max_length=10, unique=True)
    waktu_pos = models.DateField(null=True, blank=True)
    waktu_pod = models.DateField(null=True, blank=True)
    bukti_pos = models.ImageField(upload_to='static/bukti_pos/', null=True, blank=True)
    bukti_pod = models.ImageField(upload_to='static/bukti_pod/', null=True, blank=True)
    jml_paket_pos = models.PositiveIntegerField(null=True, blank=True)
    jml_paket_pod = models.PositiveIntegerField(null=True, blank=True)
    id_kurir = models.ForeignKey(Kurir, on_delete=models.CASCADE)
    barang = models.ManyToManyField(Barang)

    def __str__(self):
        return self.id_task
