from django import forms
from .models import Jogador
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from  .models import Aposta
from  .models import Time
class JogadorForm(forms.ModelForm):
      class meta:
        model = Jogador

class LoginForm(forms.Form):
    class Meta:
        model = Jogador
        fields = ('username', 'password')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))



class ApostaForm(forms.Form):
    class Meta:
        model = Aposta

    user_id = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control","readonly":"readonly","type":"hidden","id":"id_user"}))
    user_email = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control col-md-7 col-xs-12", "readonly":"readonly",   "id": "user_email"}))
    partida_id = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control","readonly":"readonly","type":"hidden","id":"id_partida"}))
    partida_descricao = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control col-md-7 col-xs-12", "readonly":"readonly",   "id": "partida_descricao"}))
    partida_data = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control col-md-7 col-xs-12", "readonly": "readonly", "id": "partida_data"}))
    aposta_valor = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control col-md-7 col-xs-12", "readonly": "readonly", "id": "aposta_valor"}))
    aposta_placar_time1 = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control col-md-7 col-xs-12",  "name": "aposta_placar_time1"}))
    aposta_placar_time2 = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control col-md-7 col-xs-12", "name": "aposta_placar_time2"}))

