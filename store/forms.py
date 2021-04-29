from django.forms import ModelForm
from django import forms
from .models import Store


class CreateStoreForm(ModelForm):
	class Meta:
		model = Store
		fields = ['owner','name','logo','description',]
