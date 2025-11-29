from django.forms import ModelForm
from .models import Animals

class AnimalsForm(ModelForm):
    class Meta:   
        model = Animals
        fields = '__all__'
    
