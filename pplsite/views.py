from django.shortcuts import render,redirect
from .forms import PlayerRegisterationForm
from .models import Player
from django.template.defaultfilters import slugify
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'pplsite/home.html')

def about(request):
    return render(request, 'pplsite/about.html')




def player_registration(request):
    if request.method == 'POST':
        form = PlayerRegisterationForm(request.POST, request.FILES)
        if form.is_valid():
            new_player = Player()
            new_player = form.save(commit=False)
            new_player.slug = slugify(new_player.email + 'tyjppp')
            new_player.save()
            messages.success(request, f'You have been registered for the auction!')
            return redirect('/')
    else:
        form = PlayerRegisterationForm()
        return render(request, 'pplsite/player_registration.html', {'form': form})

