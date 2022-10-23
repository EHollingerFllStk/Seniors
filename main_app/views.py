from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Agencies
from .forms import AddsForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def agencies_index(request):
  agencies = Agencies.objects.filter(user=request.user)
  return render(request, 'agencies/index.html', { 'agencies': agencies })

@login_required
def agencies_detail(request, agency_id):
  agency = Agencies.objects.get(id=agency_id)
  adds_form = AddsForm()
  return render(request, 'agencies/detail.html', { 'agency': agency,  'adds_form': adds_form, 
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class AgenciesCreate(LoginRequiredMixin, CreateView):
  model = Agencies
  fields =['name','address', 'phone', 'rating']
  success_url = '/agencies/'

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class AgenciesUpdate(LoginRequiredMixin,UpdateView):
  model = Agencies
  fields = ['name','address', 'phone', 'rating']

class AgenciesDelete(LoginRequiredMixin, DeleteView):
  model = Agencies
  success_url = '/agencies/'

@login_required
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

