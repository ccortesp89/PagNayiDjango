from django.http import request
from django.shortcuts import render
from .models import entrevista
from .forms import EntrevistaForm
from .resp import env
import requests
import json
# Create your views here.

def home(request):

    return render(request, 'core/home.html')

def about(request):
    # print(env())
    print(entrevista.objects.all())
    data = {
        'small': entrevista.objects.all()
    }
    return render(request, 'core/about.html', data) 



def nueva_entrevista(request):
    data = {
        'form' : EntrevistaForm()
    }

    if request.method == 'POST':
        artista = request.POST.get('artista')
        foto = request.POST.get('fotoSmall')
        fotoS = env(foto)
        print(artista)
        print(foto)
        formulario = EntrevistaForm(request.POST)
        formu = entrevista(
            artista=artista,
            fotoSmall=fotoS
        )
        if formulario.is_valid():
            # formulario.save()
            formu.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request, 'core/nueva_entrevista.html', data)

def entrevistas(request):
    return render(request, 'core/entrevistas.html')

def contact_me(request):
    return render(request, 'core/contact_me.html')