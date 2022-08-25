from django.db import models

# Create your models here.
class Kelompok(models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
class Buku(models.Model):
    judul = models.CharField(max_length=100)
    pengarang = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    tahun_terbit = models.IntegerField()
    jumlah_halaman = models.IntegerField()
    jumlah_buku = models.IntegerField()
    kategori = models.CharField(max_length=100)
    kelompok_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.judul

