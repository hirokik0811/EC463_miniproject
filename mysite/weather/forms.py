from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ['name']
		widgets = {
			'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
	    }
	def raise_error(self, error_message):
		self.error = True
		self.error_message = error_message