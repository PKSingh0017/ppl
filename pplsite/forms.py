from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Player


class PlayerRegisterationForm(ModelForm):

    class Meta:
        model = Player
        fields = ['firstname', 'lastname', 'email', 'whatsapp_no', 'year', 'branch', 'role', 'block', 'room_number', 'profile_image']
