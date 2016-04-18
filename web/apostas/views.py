from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from  .models import Jogador
from  .models import Partida
from django.shortcuts import get_object_or_404, render
from  .forms import ApostaForm
from .models import Aposta
from .models import Time
from django.shortcuts import redirect
# Create your views here.
def user_login(request):
    user = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,
                                password=password)

        if user is not None:
            if user.is_active:
                    jogador = Jogador.objects.get(pk=user.id)
                    partidas = Partida.objects.all()
                    login(request, user)
                    return  render(request, 'apostas/login.html', {'user': jogador,'partidas':partidas})

            else:
                return HttpResponse('Disabled account')

        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'apostas/login2.html', {'form': form})

def exibir_partida(request, partida_id , user_id):
    jogador = Jogador.objects.get(pk=user_id)
    partida = get_object_or_404(Partida, pk=partida_id)
    times = Time.objects.all()

    data = {"user_id":jogador.user.id,"user_email":jogador.user.email,
            "partida_id":partida.id,"partida_descricao":partida.descricao,
            "partida_data":partida.data_partida ,"aposta_valor":5}
    form = ApostaForm(data)

    return render(request, 'apostas/teste.html', {'form':form,"partida":partida,"times":times})

def aposta_new(request):
    if request.method == "POST":
        form = ApostaForm(request.POST)

        user_id = request.POST['user_id']
        partida_id = request.POST['partida_id']
        jogador = Jogador.objects.get(pk=user_id)
        time1_id = (request.POST['time1'])
        time2_id = (request.POST['time2'])
        print(time1_id)
        time1 = Time.objects.get(id=time1_id)
        time2 = Time.objects.get(id=time2_id)
        aposta_time_placar1 = request.POST['aposta_placar_time1']
        aposta_time_placar2 = request.POST['aposta_placar_time2']
        user = jogador.user
        partida = get_object_or_404(Partida, pk=partida_id)
        aposta_valor = request.POST["aposta_valor"]
        jogador.credito = jogador.credito - float(aposta_valor)
        print(jogador.credito)
        jogador.save()
        print(aposta_valor)
        aposta = Aposta(user=user,partida=partida,
                        valor=aposta_valor,placar_time_1=aposta_time_placar1,placar_time_2=aposta_time_placar2)

        aposta.save()
        aposta.time.add(time1)
        aposta.time.add(time2)
        return render(request, 'apostas/teste2.html',{"aposta":aposta})




