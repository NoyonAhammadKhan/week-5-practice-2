from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm
from django.urls import reverse_lazy
from django.views import View
# Create your views here.


@method_decorator(login_required, name="dispatch")
class AddMusian(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditMusician(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'edit_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class DeleteFromTable(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'


@method_decorator(login_required, name="dispatch")
class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form)
        form.instance.musian_id = self.kwargs.get('pk')
        return super().form_valid(form)


class Home(ListView):
    model = Musician
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musicians'] = Musician.objects.all()
        context['albums'] = Album.objects.all()
        return context
