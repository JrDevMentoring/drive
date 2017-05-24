from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from .models import Suggestion
from .forms import SuggestionForm

def home(request):
  return render(request, 'motions/home.html')

def index(request):
  if request.user.is_authenticated():
    form = SuggestionForm()
    motions_list = Suggestion.objects.order_by('-pub_date')
    context = { 'motions_list': motions_list, 'form': form }
    return render(request, 'motions/index.html', context)
  else:
    messages.error(request, 'Kindly login via slack before continuing.')
    return HttpResponseRedirect(reverse('home'))

def create(request):
  if request.user.is_authenticated():
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = SuggestionForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
        # process the data in form.cleaned_data as required
        suggestion_text = form.cleaned_data['suggestion_text']
        Suggestion.objects.create(suggestion_text=suggestion_text, pub_date=timezone.now())
        messages.success(request, 'Thank you, the suggesting has been successfully captured.')

    return HttpResponseRedirect(reverse('motions:index'))
  else:
    messages.error(request, 'Kindly login via slack before continuing.')
    return HttpResponseRedirect(reverse('home'))

def vote(request, motion_pk):
  print(motion_pk)
  if request.user.is_authenticated():
    # pk = request.GET.get('motions_pk', '')
    motion = Suggestion.objects.get(pk=motion_pk)
    user = request.user
    print(user.id)
    motion.votes.up(user.id)
    messages.success(request, 'Thanks for the vote.')
    return HttpResponseRedirect(reverse('motions:index'))
  else:
    messages.error(request, 'Kindly login via slack before continuing.')
    return HttpResponseRedirect(reverse('home'))
