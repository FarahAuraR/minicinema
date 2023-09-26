<details>
<summary>TUGAS 2</summary>
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

Pada tahap ini, pembuatan fungsi dilakukan untuk menghubungkan View dengan Template. Langkah pertama yang saya lakukan yaitu dengan membuka `views.py` dan  mengimpor fungsi render dari modul `django.shortcuts`. Langkah ini dilakukan untuk me-render tampilan HTML dengan menggunakan data yang diberikan. Setelah itu, saya lanjutkan dengan menambahkan fungsi `show_main`, seperti sebagai berikut.

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

Sebelum deploy, saya melakukan `add`, `commit`, `push` ke repositori utama `minicinema` pada GitHub. Setelah itu, saya menghubungkan Adaptable dengan repositori tersebut dan memilih `Python App Template` sebagai template deployment dan `PostgreSQL` sebagai tipe basis data yang akan digunakan. Kemudian, saya melakukan penyesuaian python version dan memasukkan perintah `python manage.py migrate && gunicorn amoron.wsgi` pada Start Command. Terakhir, saya mencentang bagian `HTTP Listener on Port` dan memulai proses deployment.

<h2>Membuat README.md</h2>

Pada tahap ini, saya membuat `README.md` yang berisi link menuju aplikasi Adaptable yang sudah di-deploy serta menjawab beberapa pertanyaan. Setelah itu, saya melakukan `add`, `commit`, `push` ke repositori utama minicinema pada GitHub.

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
</details>

<details>
<summary>TUGAS 3</summary>
<h2>Perbedaan antara form POST dan form GET dalam Django</h2>

Metode POST:
  * Data dikirim dalam badan permintaan (request body) sehingga tidak terlihat di URL
  * Lebih aman untuk mengirim data sensitif karena tidak dapat dilihat oleh pengguna
  * Biasanya digunakan untuk mengirim data yang akan memengaruhi perubahan status di server
  * Tidak terbatas oleh batasan panjang URL karena data dikirim dalam badan permintaan sehingga lebih cocok untuk mengirim data besar atau kompleks

Metode GET:
  * Data dikirim sebagai bagian dari URL dan terlihat oleh semua orang yang melihat URL tersebut
  * Tidak cocok untuk mengirim data sensitif karena kerentanannya terhadap pihak ketiga yang dapat melihat data
  * Biasanya digunakan untuk mengambil data dari server tanpa mengubah statusnya
  * Terbatas dalam kapasitas data yang dapat dikirimkan karena tergantung pada panjang URL maksimum yang didukung oleh server dan browser

Dapat disimpulkan, beberapa perbedaan antara form POST dan GET dalam Django diantarnya terkait dengan cara data dikirim, keamanan, tujuan penggunaan, dan kapasitas data yang dapat ditangani oleh masing-masing metode. Pemilihan metode tergantung pada kebutuhan aplikasi web dan tingkat keamanan yang diperlukan.


<h2>Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data</h2>

XML (eXtensible Markup Language):
  * Bahasa markup yang digunakan untuk mendefinisikan struktur data hierarkis dengan menggunakan tag untuk menandai elemen-elemen dalam data
  * Sering digunakan untuk pertukaran data antar aplikasi dan penyimpanan data yang dapat diuraikan oleh berbagai aplikasi
  * Memiliki aturan yang ketat dalam hal sintaksis serta dapat menghasilkan dokumen yang lebih berat dan sulit dibaca manusia dibandingkan dengan JSON

JSON (JavaScript Object Notation):
  * Format pertukaran data yang menggunakan struktur objek dan array yang mudah dibaca serta datanya disusun dalam pasangan nama-nilai
  * Digunakan untuk pertukaran data antara aplikasi web dan server serta sebagai format konfigurasi yang dapat dengan mudah dibaca manusia
  * Lebih ringan dan mudah dibaca dibandingkan dengan XML sehingga menjadi format yang lebih populer untuk komunikasi data di web

HTML (HyperText Markup Language):
  * Bahasa markup yang digunakan untuk membangun halaman web dan berfokus pada presentasi dan tampilan halaman web
  * Digunakan untuk membuat halaman web yang dapat diakses oleh browser web dan tidak digunakan untuk pertukaran data
  * Memiliki aturan sintaksis yang ketat, tetapi fokusnya lebih pada representasi visual daripada data mentah

Dapat disimpulkan perbedaan utama antara ketiganya, yaitu XML merupakan format yang lebih kompleks dan ketat serta cocok untuk pertukaran data yang rumit, sedangkan JSON adalah format yang lebih ringan dan mudah dibaca untuk pertukaran data serta sangat umum digunakan dalam komunikasi web modern. Di sisi lain, HTML digunakan untuk membangun halaman web tanpa tujuan utama pertukaran data.


<h2>Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?</h2>

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena formatnya yang ringan, mudah dibaca, dan mendukung berbagai jenis data. JSON juga bersifat bahasa-agnostik sehingga memudahkan komunikasi efisien antara aplikasi web yang berbeda dalam berbagai bahasa. Dukungan bawaan oleh mayoritas browser web dan dukungan yang luas oleh komunitas pengembang membuat JSON menjadi preferensi yang sangat efisien dalam pertukaran data dalam web yang dinamis dan cepat.


<h1>Step-by-Step Mengimplementasikan Tugas</h1>
<h2>Membuat Input Form untuk Menambahkan Objek Model pada App Sebelumnya</h2>

Sebelum membuat form registrasi, saya membuat skeleton yang berfungsi sebagai kerangka views dari situs web saya. Saya membuat folder `templates` pada root folder dan membuat berkas HTML baru bernama `base.html` sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek. 

Langkah selanjutnya, saya membuka `settings.py` yang ada pada subdirektori `mini_cinema`. Agar berkas `base.html` terdeteksi sebagai berkas template, saya menambahkan potongan kode `'DIRS': [BASE_DIR / 'templates']` pada baris yang mengandung `TEMPLATES`. Lalu, saya melanjutkan dengan membuka subdirektori `templates` yang ada pada direktori `main`. Saya juga melakukan beberapa perubahan pada `main.html` agar bisa menggunakan `base.html` sebagai template utama.

Untuk membuat struktur form yang dapat menerima data produk baru, langkah yang saya lakukan yaitu membuat berkas baru pada direktori `main` dengan nama `forms.py` dan membuat class serta atribut yang diperlukan seperti sebagai berikut.

```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount",  "price", "description"]
```

Saya lanjutkan dengan membuka `views.py` yang ada pada folder `main` dan menambahkan beberapa `import` yang diperlukan serta membuat fungsi baru dengan nama `create_item` pada berkas tersebut. Fungsi `create_item` yang saya buat menerima parameter `request` dan saya isi fungsi tersebut agar menghasilkan formulir yang dapat menambahkan data item secara otomatis ketika data di-submit dari form, seperti sebagai berikut.
```python
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

Lalu pada fungsi `show_main` yang sudah ada pada berkas `views.py`, saya menambahkan fungsi `Item.objects.all()` yang digunakan untuk mengambil seluruh object Item yang tersimpan pada database dan tidak lupa untuk menambahkan `key` dan `values` baru seperti sebagai berikut.
```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'name' : 'Farah Aura Rosadi',
        'class' : 'PBP D',
        'items' : items
    }

    return render(request, "main.html", context)
```

Saya melanjutkan dengan membuka `urls.py` yang ada pada folder `main` dan `import` fungsi `create_item` yang sudah dibuat. Saya juga menambahkan `path url` ke dalam `urlpatterns` pada `urls.py` di `main` untuk mengakses fungsi yang sudah di-import pada poin sebelumnya, dengan kode `path('create-product', create_product, name='create_product'),`

Kemudian saya membuat berkas HTML baru dengan nama `create_item.html` pada direktori `main/templates` untuk menampilkan fields form yang sudah dibuat pada forms.py sebagai table serta tombol submit untuk mengirimkan request ke view `create_product(request)`.
```python
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Selanjutnya, saya kembali membuka `main.html`, kemudian menambahkan kode yang sesuai untuk menampilkan data produk dalam bentuk table serta tombol "Add New Item" yang akan redirect ke halaman form, seperti sebagai berikut.

```python
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Price</th>
            <th>Description</th>
        </tr>
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.price}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    </table>
  
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
```

<h2>Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID</h2>

Langkah pertama, saya membuka `views.py` yang ada pada folder `main` dan menambahkan `import` yang dibutuhkan, yaitu sebagai berikut.
```python
from django.http import HttpResponse
from django.core import serializers
```

Kemudian saya membuat beberapa fungsi yang menerima parameter `request` (untuk XML by ID dan JSON by ID menerima parameter tambahan yaitu `id`) dan membuat sebuah variabel di dalam masing-masing fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada `Item`. Saya juga menambahkan `return` function berupa `HttpResponse` yang berisi parameter data hasil query, seperti sebagai berikut.

```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```


<h2>Membuat routing URL untuk masing-masing views yang telah ditambahkan</h2>

Dalam membuat routing URL, saya membuka `urls.py` yang ada pada folder `main` dan `import` semua fungsi yang sudah dibuat serta menambahkan `path url` ke dalam `urlpatterns` untuk mengakses fungsi yang sudah di-import, seperti sebagai berikut.

```python
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

<h1>Mengakses URL Menggunakan Postman dan Screenshot Hasil</h1>

Langkah pertama, saya memastikan server sudah berjalan. Kemudian, saya membuka Postman dan melakukan request baru dengan method `GET` dengan url http://localhost:8000
[![html1.png](https://i.postimg.cc/vBM5DT2t/html1.png)](https://postimg.cc/2qc1KkD1)
[![html2.png](https://i.postimg.cc/GtT3CJP7/html2.png)](https://postimg.cc/8fDgdv0M)

Selanjutnya, url http://localhost:8000/xml
[![xml.png](https://i.postimg.cc/prNXttNn/xml.png)](https://postimg.cc/xJRSKh10)

Lalu, url http://localhost:8000/json
[![json.png](https://i.postimg.cc/ZRHjGJvw/json.png)](https://postimg.cc/XGZwFS85)

Terakhir, url http://localhost:8000/xml/1 dan http://localhost:8000/json/2 untuk mengetes fungsi pengambilan data produk berdasarkan ID.
[![xml1.png](https://i.postimg.cc/3NC754CP/xml1.png)](https://postimg.cc/1VtbDzdH)
[![json2.png](https://i.postimg.cc/KcV8nBR8/json2.png)](https://postimg.cc/dD2FF72b)


<h1>Bonus</h1>

Langkah yang saya lakukan dalam mengimplementasikan bonus yaitu dengan membuka `main.html` pada direktori `main/templates`, kemudian saya menambahkan baris kode `<h4>You've added {{ items.count }} movie(s) to your Mini Cinema experience.</h4>` sehingga akan menampilkan jumlah item yang tersimpan pada aplikasi.

</details>

<details>

<summary>TUGAS 4</summary>


<h1>Pengertian, Kelebihan, Kekurangan Django UserCreationForm</h1>
Django UserCreationForm adalah salah satu fitur yang disediakan oleh Django untuk membuat pengguna baru yang dapat menggunakan aplikasi web. Form ini memiliki tiga bidang: username, password1, dan password2 (biasanya digunakan untuk konfirmasi password).

Kelebihan :
  * Memiliki validasi terintegrasi yang kuat untuk memeriksa dan validasi data pengguna secara otomatis, mengurangi risiko masalah keamanan dan integritas data.
  * Customizable, memungkinkan penyesuaian bidang tambahan dan perilaku validasi sesuai dengan kebutuhan proyek.
  * Mudah diintegrasikan dengan sistem otentikasi Django, memungkinkan pengguna terdaftar untuk langsung menggunakan otentikasi Django.
    
Kekurangan :
  * Keterbatasan fitur bawaan, hanya mencakup informasi dasar, sehingga memerlukan penambahan bidang tambahan secara manual atau pembuatan formulir kustom untuk informasi tambahan.
  * Tampilan standar yang mungkin tidak cocok dengan desain atau tata letak situs web, memerlukan pekerjaan tambahan untuk menyesuaikan tampilan formulir.
  * Validasi kustom yang kompleks atau aturan bisnis yang rumit memerlukan penambahan validasi manual yang memerlukan waktu dan usaha.
  * Kompleksitas konfigurasi, terutama untuk proyek dengan persyaratan yang sangat khusus, mungkin dianggap sulit oleh beberapa pengembang.


<h1>Perbedaan Autentikasi dan Otorisasi dalam konteks Django</h1

Autentikasi adalah proses verifikasi identitas pengguna, sedangkan otorisasi mengendalikan akses pengguna ke data atau fitur dalam aplikasi. Autentikasi memeriksa siapa pengguna tersebut, sementara otorisasi menentukan apa yang dapat mereka lakukan setelah diautentikasi. Keduanya penting untuk menjaga keamanan dan kontrol akses dalam aplikasi web. Autentikasi memastikan pengguna adalah yang mereka klaim, sementara otorisasi memastikan pengguna hanya dapat mengakses atau mengubah hal-hal yang mereka berhak akses sesuai dengan peran dan izin mereka.

<h1>Cookies dalam konteks aplikasi web dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna</h1>

Dalam konteks aplikasi web, cookies adalah file kecil yang disimpan di sisi klien (browser pengguna) dan digunakan untuk menyimpan informasi. Django, sebagai framework web Python, menggunakan cookies untuk mengelola data sesi pengguna. 

Dalam Django, data sesi pengguna disimpan dengan aman di dalam sesi, dan pengguna diidentifikasi melalui cookies yang mengandung data sesi saat setiap permintaan ke aplikasi dikirim. Django mengamankan data sesi dengan mengenkripsinya sehingga hanya server Django yang dapat mengakses dan mendekripsi informasi tersebut, menjaga kerahasiaan pengguna. Pengembang juga memiliki fleksibilitas untuk mengonfigurasi berbagai aspek pengelolaan sesi, termasuk cara penyimpanan, waktu kadaluarsa, dan pengaturan lainnya sesuai dengan kebutuhan aplikasi mereka.

Penggunaan cookies dan modul sesi Django memungkinkan pengembang untuk mengelola data sesi pengguna dengan aman dan efisien, yang berguna untuk sesi login, keranjang belanja, dan personalisasi aplikasi web.

<h1>Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?</h1>

Penggunaan cookies dalam pengembangan web memiliki potensi risiko yang perlu diwaspadai, tetapi dapat menjadi aman jika dikelola dengan benar. Cookies memiliki tingkat keamanan default seperti "HttpOnly" dan "Secure" yang membantu melindungi dari serangan umum seperti CSRF. Penting untuk memastikan bahwa data sensitif tidak disimpan dalam cookies, menghapus cookies yang tidak diperlukan secara teratur, dan memiliki kebijakan privasi yang jelas. Pemantauan dan pelaporan insiden keamanan juga merupakan langkah penting untuk menjaga keamanan pengguna. Dengan tindakan pencegahan yang tepat, penggunaan cookies dapat diintegrasikan secara aman dalam aplikasi web untuk meningkatkan fungsionalitas tanpa mengorbankan keamanan pengguna.

<h1>Step-by-Step Mengimplementasikan Tugas</h1>

<h2>Mengimplementasikan Fungsi Registrasi, Login, dan Logout</h2>

Untuk mengimplementasikan fungsi `registrasi`, `login`, dan `logout`, langkah pertama yang saya lakukan yaitu dengan membuka `views.py` yang ada pada subdirektori main dan membuat ketiga fungsi. Pertama, fungsi `register` yang menerima parameter request untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form. Kedua, fungsi `login_user` yang berfungsi untuk mengautentikasi pengguna yang ingin login. Terakhir, fungsi `logout_user` untuk melakukan mekanisme logout. Selain itu, saya juga meng-import yang diperlukan, seperti sebagai berikut.

```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Kemudian, saya lanjutkan dengan membuat berkas HTML bernama `register.html` pada folder main/templates dan mengisinya dengan kode sebagai berikut.

```python
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Saya juga membuat berkas HTML bernama `login.html` pada folder main/templates dan mengisinya dengan kode sebagai berikut.

```python
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

Lalu, saya membuka `urls.py` yang ada pada subdirektori main dan impor fungsi yang sudah dibuat yaitu
`from main.views import register, login_user, logout_user`

Pada berkas `main.html` di main/templates, setelah hyperlink tag untuk Add New Product, saya menambahkan potongan kode berikut.

```python
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

Saya juga menambahkan 3 path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.

```python
path('register/', register, name='register'), 
path('login/', login_user, name='login'), 
path('logout/', logout_user, name='logout'),
```

Terakhir, pada `views.py` di atas fungsi `def show_main(request):`, saya menambahkan `@login_required(login_url='/login')` agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).


<h2>Membuat 2 Akun Pengguna dengan 3 Dummy Data</h2>

Langkah pertama, saya menjalankan `python manage.py runserver` di terminal direktori `minicinema`. Setelah itu, saya membuka `http://localhost:8000/` dan mulai melakukan register. Register ini dilakukan pada `register.html` yang telah saya buat. Saya membuat dua akun dengan username `farah` dan `aura`. Setelah akun berhasil dibuat, saya melakukan login pada masing-masing akun, tampilan login ini sesuai dengan `login.html` yang telah saya buat. Terakhir, saya menambahkan tiga dummy data dengan klik tombol `Add New Product`.

<h2>Menghubungkan Model Item dengan User</h2>

Pada tahap ini, saya menghubungkan setiap objek Item yang akan dibuat dengan pengguna yang membuatnya agar pengguna yang sedang terotorisasi hanya melihat item yang telah dibuat sendiri. Dalam implementasinya, saya membuka `models.py` yang ada pada subdirektori main dan mengimpor model dengan `from django.contrib.auth.models import User`. Setelah itu, pada model Item yang sudah dibuat, saya menambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` Hal ini berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah relationship, dimana sebuah produk pasti terasosiasikan dengan seorang user. Pada `views.py` yang ada pada subdirektori main, saya juga mengubah kode pada fungsi `create_item` menjadi seperti sebagai berikut.

```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

Setelah itu, saya mengubah beberapa bagian pada fungsi `show_main` menjadi sebagai berikut.

```python
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
```

Lalu, saya simpan semua perubahan dan lakukan migrasi model dengan `python manage.py makemigrations`.
Ketika muncul error saat melakukan migrasi model, saya ketik `1` untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data. Kemudian, saya ketik angka `1` lagi untuk menetapkan user dengan ID 1 (yang sudah dibuat sebelumnya) pada model yang sudah ada. Setelah itu, saya lakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.


<h2>Menampilkan Detail Informasi Pengguna yang sedang Logged In dan Menerapkan Cookies</h2>

Langkah pertama, saya buka `views.py` yang ada pada subdirektori `main` dan tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime`.

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

Pada fungsi `login_user` saya mengganti kode yang ada pada blok `if user is not None` untuk menambahkan cookie `last_login` agar dapat melihat kapan terakhir kali pengguna melakukan login

```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

Pada fungsi `show_main`, saya juga menambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel context.

```python
...
    context = {
        'name': request.user.username,
        'class' : 'PBP D',
        'items' : items,
        'last_login': request.COOKIES['last_login'],
    }
...
```

Selanjutnya, saya mengubah fungsi `logout_user` menjadi seperti berikut.

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Terakhir, saya kembali membuka berkas `main.html`. Kemudian, di antara tabel dan tombol logout, saya menambahkan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` untuk menampilkan data last login.


<h1>Bonus</h1>
Implementasi bonus untuk menambahkan amount dan menghapus suatu objek dari inventori.

[![bonus.png](https://i.postimg.cc/5yVzTJ9d/bonus.png)](https://postimg.cc/mzmh10F8)

</details>

