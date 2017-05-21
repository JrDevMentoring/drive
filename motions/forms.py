from django import forms

class SuggestionForm(forms.Form):
    suggestion_text = forms.CharField(label='Add a motion', max_length=500)
