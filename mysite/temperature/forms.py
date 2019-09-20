from django.forms import ModelForm, TextInput
from .models import Room, Interval

class RoomForm(ModelForm):
	class Meta:
		model = Room
		fields = ['name']
		widgets = {
			'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Room Name'}),
	    }
	def raise_error(self, error_message):
		self.error = True
		self.error_message = error_message
		
class IntervalForm(ModelForm):
	class Meta:
		model = Interval
		fields = ['interval']
		widgets = {
			'interval' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Interval'}),
	    }
	def raise_error(self, error_message):
		self.error = True
		self.error_message = error_message