from django import forms
from .models import Car
#from django.contrib.auth.models import User


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value',"O valor do carro deve ser maior ou igual a R$ 10.000,00.")
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year',"O ano de fabricação deve ser maior ou igual a 1975.")
        return factory_year
   
    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year < 1975:
            self.add_error('model_year',"O ano do modelo deve ser maior ou igual a 1975.")
        return model_year
   
       