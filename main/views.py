import json
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from main.forms import ItemForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

from main.models import Item

from django.contrib.auth.models import User

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class' : 'PBP D',
        'items' : items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

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

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('main:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')

        else:
            messages.info(request, 'Password not matching..')
            return redirect('main:register')
    else:
        return render(request, 'register.html')

@csrf_exempt
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

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.amount >= 0:
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def reduce_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def remove_item(request, item_id):
    if request.method == 'POST' and 'remove' in request.POST:
        item = Item.objects.get(id = item_id)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_item(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def get_item_json(request):
    items = Item.objects.filter(user=request.user)
    item_list = []
    for item in items:
        item_dict = {
            'pk': item.pk,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'amount': item.amount,
            'edit_url': reverse('main:edit_item', args=[item.pk]),
            'delete_url': reverse('main:delete_item', args=[item.pk]),
        }
        item_list.append(item_dict)
    return JsonResponse(item_list, safe=False)

...
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return HttpResponse("Created", status=201)
        else:
            # Handle form validation errors and return as JSON
            errors = form.errors.as_json()
            return HttpResponseBadRequest(errors, content_type='application/json')

    return HttpResponseNotFound()
