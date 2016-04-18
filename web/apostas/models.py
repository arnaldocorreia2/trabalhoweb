from django.db import models
from django.contrib.auth.models import User

class Jogador(models.Model):
    user = models.OneToOneField(User)
    credito = models.FloatField(default=10)




class Time(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Partida(models.Model):
    user = models.OneToOneField(User)
    time = models.ManyToManyField(Time)
    descricao = models.CharField(max_length=100)
    data_partida = models.DateField()

    def __str__(self):
        return self.descricao


class Aposta(models.Model):
    user = models.OneToOneField(User)
    partida = models.OneToOneField(Partida)
    valor = models.FloatField(default=10)
    time = models.ManyToManyField(Time)
    placar_time_1 =  models.IntegerField()
    placar_time_2 = models.IntegerField()

class Resultado(models.Model):
    partida = models.ManyToManyField(Partida)
    times = models.ManyToManyField(Time)
    valor_gol_time = models.IntegerField()
