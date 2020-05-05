from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy
from basic_app import models

# Create your views here.
# def index(request):
#     return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['hello'] = 'Hello world!'
        return context

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ['name','principal','location']
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ['name','principal']
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
