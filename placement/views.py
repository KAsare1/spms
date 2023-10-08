from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from placement.forms import MyForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# @login_required
# def my_form(request):
#   form = MyForm(request.POST, request.FILES)
#   if form.is_valid():
#     print('hello world')
#     form.save()
#   return render(request=request, template_name='home.html', context={'form': form})

@login_required
def placement_save(request):
  form = MyForm(request.POST, request.FILES)
  if form.is_valid():
    print(request.POST)
    print('hello world')
    form.save()
  return render(request=request, template_name='home.html', context={'form': form})