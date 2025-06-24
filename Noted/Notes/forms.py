from django.forms import ModelForm
from .models import Note_data

class note_form(ModelForm):
    class Meta:
        model = Note_data
        exclude = ['user']