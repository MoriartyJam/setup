from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ClientForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Client
from django.contrib import messages


@csrf_exempt
def index(request):
    form = ClientForm
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            name = form.cleaned_data['name']
            request.session['name'] = name
            request.session.set_expiry(30)
            # request.session.save()

            form.save()
            messages.success(request, f'Hello {email}!')
            return redirect('/', {'form': form})
        else:
            name = request.POST.get('name')
            messages.error(request, f'Already saw you {name} ')
            return redirect('/', {'form': form})


    else:
        form = ClientForm()
    return render(request, 'create.html', {'form': form})


def name_list(request):
    clients = Client.objects.all
    return render(request, 'name_list.html', {'clients': clients})


