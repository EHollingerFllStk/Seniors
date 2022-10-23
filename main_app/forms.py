from django.forms import ModelForm
from .models import Adds

class AddsForm(ModelForm):
  class Meta:
    model = Adds
    fields = ['date', 'service']
    