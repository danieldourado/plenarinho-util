from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import FalasForm
from .models import Falas


class FalasList(ListView):
    model = Falas
    paginate_by = 20


class FalasCreate(CreateView):
    model = Falas
    form_class = FalasForm
    success_url = reverse_lazy('jogo_cidadania:list')


class FalasDetail(DetailView):
    model = Falas


class FalasUpdate(UpdateView):
    model = Falas
    form_class = FalasForm
    success_url = reverse_lazy('jogo_cidadania:list')


class FalasDelete(DeleteView):
    model = Falas
    success_url = reverse_lazy('jogo_cidadania:list')
