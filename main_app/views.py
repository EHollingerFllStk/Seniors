from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Agencies
from .forms import AddsForm


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def agencies_index(request):
  agencies = Agencies.objects.all()
  return render(request, 'agencies/index.html', { 'agencies': agencies })

def agencies_detail(request, agency_id):
  agency = Agencies.objects.get(id=agency_id)
  adds_form = AddsForm()
  return render(request, 'agencies/detail.html', { 'agency': agency,  'adds_form': adds_form, 
  })

class AgenciesCreate(CreateView):
  model = Agencies
  fields =['name','address', 'phone', 'rating']
  success_url = '/agencies/'

class AgenciesUpdate(UpdateView):
  model = Agencies
  fields = ['name','address', 'phone', 'rating']

class AgenciesDelete(DeleteView):
  model = Agencies
  success_url = '/agencies/'

def add_adds(request, agency_id):
  form = AddsForm(request.POST)
  if form.is_valid():
    new_adds = form.save(commit=False)
    new_adds.agency_id = agency_id
    new_adds.save()
  return redirect('detail', agency_id=agency_id)








# class Agencies:
#   def __init__(self, name, address, phone, rating):
#     self.name = name
#     self.address = address
#     self.phone = phone
#     self.rating = rating

# agencies = [
#   Agencies('First Light Home Care','555 Bryn Mawr Ave. Bryn Mawr, PA 19634', '610-638-0638', 3),
#   Agencies('Visiting Angels Home Care','521 Bryn Mawr Ave. Bryn Mawr, PA 19634', '610-638-0639', 3),
#   Agencies('Senior Living Home Health Care','523 Bryn Mawr Ave. Bryn Mawr, PA 19634', '610-638-0631', 4),
# ]

