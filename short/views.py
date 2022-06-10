import random
import string
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView

)
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from short.forms import UrlForm, UserRegisterForm
from short.models import Url 
# Create your views here.

class HomeView(TemplateView):
    template_name = "short/layout/home.html"



    
class BaseView(LoginRequiredMixin,View):
    model = Url
    fields = '__all__'
    success_url = reverse_lazy('url-list')

class UrlListView(BaseView,ListView):
    template_name = "short/pages/url_list.html"
    
class UrlCreateView(BaseView,CreateView):
    template_name = "short/pages/url_form.html"
    fields = ['url']

class UrlDetailView(BaseView,DetailView):
    template_name = "short/pages/url_detail.html"

class UrlUpdateView(BaseView,UpdateView):
    template_name = "short/pages/url_form.html"

class UrlDeleteView(BaseView,DeleteView):
    template_name = "short/pages/url_confirm_delete.html"

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(
                request, f"The account has been created")
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'short/auth/register.html', context)

@login_required
def CreateShortUrl(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                        for x in range(10))
            url = form.cleaned_data["url"]
            new_url = Url(url=url, slug=slug)
            new_url.save()
            messages.success(
                request, f"The url has been updated ")
            # return redirect('url-show')
            return redirect('url-list')
    
            
    else:
        form = UrlForm()

    context = {
        'form': form
    }
    return render(request, 'short/pages/url_form.html', context)

@login_required
def NewShortUrl(request):

    new_url = Url.objects.values('slug')
    # context = {
    #     'new_url':new_url
    # }
    return render(request, 'short/pages/url_show.html', {'new_url':new_url})
