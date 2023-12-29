from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    image_file = forms.ImageField(label='Image Upload', required=False, widget=forms.FileInput(attrs={'class': 'form-control',
                                                                                                       'accept':'image/*', 
                                                                                                       }))

    class Meta:
        model = Image
        fields = ['image_file']
