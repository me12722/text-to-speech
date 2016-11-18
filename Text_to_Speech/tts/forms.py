from django.forms import ModelForm
from .models import MP3

class Mp3DetailsForm(ModelForm):

    class Meta:
        model = MP3
        fields = ('file_name', 'text',)
