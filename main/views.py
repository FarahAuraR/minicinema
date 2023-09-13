from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Farah Aura Rosadi',
        'class' : 'PBP D'
    }

    return render(request, "main.html", context)
