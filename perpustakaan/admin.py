from typing import List
from django.contrib import admin
from .models import Kelompok, Buku

# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display: = ['judul', 'pengarang', 'penerbit', 'tahun_terbit', 'jumlah_halaman', 'jumlah_buku', 'kategori', 'kelompok_id']
    search_fields = ['judul', 'pengarang', 'penerbit', 'tahun_terbit', 'jumlah_halaman', 'jumlah_buku', 'kategori', 'kelompok_id']
    list_filter = ('kelompok_id')
    list_per_page: int = 5
    

admin.site.register(Kelompok, BukuAdmin)
admin.site.register(Buku)
