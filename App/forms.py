from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = ['name', 'description', 'address', 'images']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Name'}),
			'description': forms.Textarea(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Description', 'rows': 6}),
			'address': forms.Textarea(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Address', 'rows': 2}),
			'images': forms.FileInput(attrs={'class': 'mt-1 mb-4', 'multiple': True}),
		}