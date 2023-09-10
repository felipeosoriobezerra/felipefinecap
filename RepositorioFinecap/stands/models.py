from django.db import models

class Stand(models.Model):
    localizacao = models.TextField(max_length=150)
    valor = models.FloatField(max_length=1000)

    def __str__(self):
        return self.localizacao
  

class Reserva(models.Model):
    nome_empresa = models.TextField(max_length=150)
    categoria_empresa = models.TextField(max_length=150)
    cnpj = models.CharField(max_length=11)
    quitado = models.BooleanField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_empresa