from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Scrap


class ScrapListView(ListView):
    model = Scrap
    template_name = "scrapwall.html"
    context_object_name = 'scrap'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name', )
        except KeyError:
            a = None
        if a:
            scrap = Scrap.objects.filter(
                title__icontains=a,

            )
        else:
            scrap = Scrap.objects.all()
        return scrap


class ScrapDetailView(DetailView):
    model = Scrap

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ScrapCreatView(CreateView):
    model = Scrap
    fields = ['title', 'content']
    get_absolute_url = '/home'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ScrapCreatView, self).form_valid(form)

    def get_success_url(self):
        return reverse('scrap-detail', kwargs={'slug': self.object.slug})


class UserScrapListView(ListView):
    model = Scrap
    template_name = "scrapwall.html"
    context_object_name = 'scrap'

    def get_queryset(self):
        scrap = Scrap.objects.filter(
                user=self.request.user)
        return scrap
