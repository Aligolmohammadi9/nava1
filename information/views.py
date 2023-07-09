from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm 
from .models import UserModel, Class
from django.views.generic import CreateView

# Create your views here.



class HomeView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'information/index.html'
    success_url = 'myapp/index.html'
    
  

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'information/success.html')
    else:
        form = UserForm()
    return render(request, 'information/index.html', {'form': form})

    
def get_price(request):
    course_id = request.GET.get('course_id')
    try:
        course = Class.objects.get(id=course_id)
        price = Class.price
    except Course.DoesNotExist:
        price = None
    return JsonResponse({'price': price})