from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import Suggestion
from .forms import SuggestionForm

def home(request):
  return render(request, 'motions/home.html')

def index(request):
  form = SuggestionForm()
  motions_list = Suggestion.objects.order_by('-pub_date')
  context = { 'motions_list': motions_list, 'form': form }
  return render(request, 'motions/index.html', context)

def create(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = SuggestionForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      # process the data in form.cleaned_data as required
      suggestion_text = form.cleaned_data['suggestion_text']
      Suggestion.objects.create(suggestion_text=suggestion_text, pub_date=timezone.now())

  return HttpResponseRedirect(reverse('motions:index'))
