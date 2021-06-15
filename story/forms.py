from django.forms import forms


class StoryForm(forms.Form):
    image = forms.ImageField()