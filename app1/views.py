from django.http import HttpResponse
from django.shortcuts import render
from app1.forms import *
from django.views.generic import TemplateView,FormView

# Create your views here.

class form_view(FormView):
    template_name='form_temp.html'
    form_class=StudentForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('data is inserted successfully')
    
class collect_url_data(FormView):
    template_name='collect_url_data'
    form_class=StudentForm
    context_object_name=''