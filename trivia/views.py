from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TriviaForm
from .models import Trivia


class TriviaList(ListView):
    model = Trivia
    paginate_by = 20


class TriviaCreate(CreateView):
    model = Trivia
    form_class = TriviaForm
    success_url = reverse_lazy('trivia:list')


class TriviaDetail(DetailView):
    model = Trivia


class TriviaUpdate(UpdateView):
    model = Trivia
    form_class = TriviaForm
    success_url = reverse_lazy('trivia:list')


class TriviaDelete(DeleteView):
    model = Trivia
    success_url = reverse_lazy('trivia:list')
