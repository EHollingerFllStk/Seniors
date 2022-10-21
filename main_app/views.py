from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello World')

def about(request):
  return render(request, 'about.html')

def agencies_index(request):
  return render(request, 'agencies/index.html', { 'agencies': agencies })

class Agencies:
  def __init__(self, name, address, phone, rating):
    self.name = name
    self.address = address
    self.phone = phone
    self.rating = rating

agencies = [
  Agencies('First Light Home Care','555 Bryn Mawr Ave. Bryn Mawr, PA 19634', '610-638-0638', 3),
  Agencies('Visiting Angels Home Care','521 Bryn Mawr Ave. Bryn Mawr, PA 19634', '610-638-0638', 3),
  Agencies('Senior Living Home Health Care','523 Bryn Mawr Ave. Bryn Mawr, PA 19634', '610-638-0638', 4),
]