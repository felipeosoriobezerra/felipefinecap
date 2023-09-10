from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import ReservaForm

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar') 


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
        return redirect('reserva_listar') 
    else:
        form = ReservaForm()
    

    return render(request, "reserva/form.html", {'form': form})

def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)
   
    if request.method == 'POST':
        form = ReservaForm(request.POST,instance=Reserva)

        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'reserva/detalhe.html',{'form':form})

def reserva_listar(request):
    reserva = Reserva.objects.all()
    context ={
        'reserva':reserva
    }
    return render(request, "reserva/visualizar.html",context)



def index(request):
    total_reserva = Reserva.objects.count()
    context = {
        'total_reserva' : total_reserva,    
    }
    return render(request, "reserva/index.html",context)

