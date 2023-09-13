
<h1>Link Adaptable</h1>
https://mini-cinema.adaptable.app

<h1>Step-by-Step Mengimplementasikan Tugas</h1>
<h2>Membuat Proyek Django</h2>
Dalam pembuatan proyek django, langkah pertama yang saya lakukan yaitu membuat direktori yang diinisiasi dengan git. Dalam direktori tersebut, saya mengaktifkan Virtual Environment menggunakan Terminal. Setelah itu, saya menambahkan beberapa dependencies.

Terakhir, saya membuat proyek Django bernama minicinema dengan menjalankan perintah `django-admin startproject minicinema .`

<h2>Membuat Aplikasi Main pada Proyek Django</h2>

Pada tahap pembuatan aplikasi main, saya menjalankan perintah `python manage.py startapp main` sehingga terbentuk direktori baru dengan nama main yang akan berisi struktur awal untuk aplikasi saya. Kemudian, saya mendaftarkan aplikasi main ke dalam proyek dengan menambahkan `main` ke list `INSTALLED_APPS` pada `settings.py.`

<h2>Melakukan Routing pada Proyek</h2>

Untuk melakukan routing pada proyek, saya membuka `urls.py` di dalam direktori proyek dan mengimpor fungsi `include` dari `django.urls`. Lalu, saya mengambahkan rute URL untuk mengarahkan ke tampilan main, seperti sebagai berikut.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main/', include('main.urls')),
]
```

`urls.py` pada proyek bertanggung jawab untuk mengatur rute URL tingkat proyek.


<h2>Membuat Model pada Aplikasi Main</h2>

Pada langkah ini, saya membuka `models.py` yang terdapat di dalam direktori aplikasi main lalu mengisinya dengan mendefinisikan model baru, seperti sebagai berikut.

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
```
Pada kode tersebut, saya mendefinisikan model dengan nama Item.
`name` , `amount`, `price`, dan `description` adalah atribut yang saya gunakan.
Langkah berikutnya yang saya lakukan yaitu migrasi model.



<h2>Membuat Fungsi untuk Dikembalikan ke Template HTML</h2>

Pada tahap ini, pembuatan fungsi dilakukan untuk menghubungkan View dengan Template. Langkah pertama yang saya lakukan yaitu dengan membuka `views.py` dan  mengimpor fungsi render dari modul django.shortcuts. Langkah ini dilakukan untuk me-render tampilan HTML dengan menggunakan data yang diberikan. Setelah itu, saya lanjutkan dengan menambahkan fungsi `show_main`, seperti sebagai berikut.

```python
def show_main(request):
context = {
	'name': 'Farah Aura Rosadi',
	'class': 'PBP D'
}
return render(request, "main.html", context)
```

Fungsi `show_main` akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai. Terakhir, saya membuka `main.html` yang telah dibuat sebelumnya dalam direktori templates pada direktori main. Saya mengubah `main.html` agar dapat menampilkan data yang sesuai.



<h2>Membuat Routing pada Aplikasi Main</h2>

Untuk membuat routing pada aplikasi main , saya membuka `urls.py` di dalam direktori main dan mengisinya dengan kode berikut.

```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
   	 path('', show_main, name='show_main'),
]
```

Hal ini dilakukan untuk memetakan fungsi yang telah dibuat pada `views.py`. 
Jadi, `urls.py` pada aplikasi akan mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi saya 

<h2>Melakukan deployment ke Adaptable</h2>
Sebelum deploy, saya melakukan add, commit, push ke repositori utama minicinema pada GitHub. Setelah itu, saya menghubungkan Adaptable dengan repositori tersebut dan memilih Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data yang akan digunakan. Kemudian, saya melakukan penyesuaian python version dan memasukkan perintah python manage.py migrate && gunicorn amoron.wsgi pada Start Command. Terakhir, saya mencentang bagian HTTP Listener on Port dan memulai proses deployment.

<h2>Membuat README.md</h2>
Pada tahap ini, saya membuat README.md yang berisi link menuju aplikasi Adaptable yang sudah di-deploy serta menjawab beberapa pertanyaan. Setelah itu, saya melakukan add, commit, push ke repositori utama minicinema pada GitHub.

<h1>Request Client ke Web Aplikasi Berbasis Django</h1>


[![bagan.jpg](https://i.postimg.cc/d3Fmx26c/Bagan.jpg)](https://postimg.cc/TLkDyWBt)

<h3>Penjelasan </h3>

  * urls.py : Mengatur alamat URL dan mengarahkan permintaan client ke views yang sesuai
  * views.py : Berisi fungsi-fungsi tampilan yang memproses permintaan client dan mengembalikan respons serta interaksi dengan models.py jika diperlukan
  * models.py : Mendefinisikan struktur data dalam aplikasi dan berfungsi sebagai abstraksi data serta menguhungkan ke database
  * Template : Mengatur tampilan halaman web yang akan ditampilkan kepada client, menggunakan sintaks template Django untuk menampilkan data dari views dan models

Kesimpulannya, dalam pengembangan aplikasi web berbasis Django, `urls.py` mengatur rute URL dan mengarahkan permintaan client ke `views.py`, di mana fungsi-fungsi tampilan memproses permintaan dan menghasilkan respons. Views dapat berinteraksi dengan `models.py` untuk mengakses data. `Template` atau berkas HTML digunakan untuk mengatur tampilan halaman web yang sesuai. Semua berkas ini bekerja sama untuk mengelola permintaan client dan merender tampilan web yang dinamis.


<h1>Penggunaan Virtual Environment </h1>

Virtual Environment adalah konsep yang sangat berguna dalam pengembangan aplikasi web berbasis Django dan proyek Python lainnya. Hal ini menciptakan lingkungan terisolasi yang memungkinkan pengembang untuk mengelola dependensi yang berbeda-beda antar proyek pada satu sistem operasi. Dengan virtual environment, proyek-proyek dapat dijalankan tanpa memengaruhi konfigurasi sistem utama. Selain itu, virtual environment juga membantu mengisolasi proyek, mengelola dependensi, dan menjaga konsistensi pengembangan. Sebenarnya kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun sangat disarankan untuk menggunakannya karena akan meningkatkan keamanan, stabilitas, dan manajemen proyek dengan menghindari konflik paket dan versi antar proyek. Oleh karena itu, penggunaan virtual environment sangat direkomendasikan dalam pengembangan aplikasi web Django dan proyek Python lainnya.

<h1>MVC, MVT, dan MVVM</h1>


MVC, MVT, dan MVVM adalah tiga pola arsitektur software yang banyak digunakan oleh para developer untuk mengorganisasi dan mengembangkan aplikasi. 
Pola-pola ini membantu dalam memisahkan komponen-komponen aplikasi, meningkatkan keterbacaan kode, memudahkan pemeliharaan, dan memungkinkan pengembangan yang lebih terstruktur sehingga mempermudah pengembangan dan evolusi aplikasi secara efisien.

MVC (Model-View-Controller)
  * Model: Komponen ini berisi logika bisnis dan data aplikasi. Berinteraksi dengan controller, database, dan terkadang memperbarui tampilan aplikasi.
  * View: Bertanggung jawab atas antarmuka pengguna (UI) dengan HTML/CSS/XML. Berkomunikasi dengan controller, dan tugasnya meliputi menampilkan data yang sesuai dan menciptakan tampilan dinamis.
  * Controller: Bertindak sebagai perantara antara view dan model. Menerima input dari view, memprosesnya melalui model, dan mengirim hasilnya kembali ke view untuk ditampilkan kepada pengguna.


MVVM (Model-View-ViewModel)
  * Model: Berisi data dasar yang diperlukan oleh perangkat lunak.
  * View: Antarmuka grafis yang berkomunikasi dengan pengguna dan menampilkan hasil dari data yang diproses.
  * ViewModel: Menyajikan abstraksi dari View, menggabungkan Model menjadi bentuk yang dapat ditampilkan di View, dan berisi perintah untuk memengaruhi Model.


MVT (Model-View-Template):
  * Model: Komponen yang mengelola data dan aturan bisnis aplikasi.
  * View: Antarmuka pengguna (UI) yang menampilkan data dengan menggunakan Template (tampilan HTML dengan markup).
  * Template: Tampilan HTML yang digunakan untuk menampilkan data dari Model. Template tidak memiliki logika bisnis yang signifikan dan fokus pada presentasi data.

Perbedaan utama di antara ketiganya adalah cara komponen-komponen tersebut berinteraksi satu sama lain dan sejauh mana mereka memisahkan tanggung jawab dalam aplikasi. MVC memiliki pengendali (Controller) yang menghubungkan Model dan View. MVVM memiliki ViewModel yang lebih abstrak dan kuat dalam mengisolasi View dari Model, sedangkan MVT adalah varian yang lebih sederhana dengan Template yang bertanggung jawab untuk presentasi data. Pemilihan pola tergantung pada kebutuhan proyek dan preferensi pengembang.
