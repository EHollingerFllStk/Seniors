from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Agencies

# Create your views here.

def home(request):
  return render('<h1>Hello World</h1>')

def about(request):
  return render(request, 'about.html')

def agencies_index(request):
  agencies = Agencies.objects.all()
  return render(request, 'agencies/index.html', { 'agencies': agencies })

def agencies_detail(request, agency_id):
  agency = Agencies.objects.get(id=agency_id)
  return render(request, 'agencies/detail.html', { 'agency': agency })

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