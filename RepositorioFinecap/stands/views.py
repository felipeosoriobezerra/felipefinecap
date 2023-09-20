from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


class ReservaCreateView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "reserva/form.html"

    def form_valid(self, form):
        messages.success(self.request, "Reserva realizada!!!")
        return super().form_valid(form)



class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "reserva/visualizar.html"

class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("lista_reservas")

    def form_valid(self, form):
        messages.warning(self.request, "Reserva Deletada!!!")
        return super().form_valid(form)

class ReservaUpdateView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "reserva/form.html"

    def form_valid(self, form):
        messages.success(self.request, "Alterações cadastradas!")
        return super().form_valid(form)


class ReservaDetailView(generic.DetailView):
    model = Reserva
    template_name = "reserva/detalhe.html"  


def index(request):
    total_reserva = Reserva.objects.count()
    context = {
        'total_reserva' : total_reserva,    
    }
    return render(request, "reserva/index.html",context)

