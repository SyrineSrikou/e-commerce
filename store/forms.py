from django.forms import ModelForm
from django import forms
from .models import Store, Product


class CreateStoreForm(ModelForm):
	class Meta:
		model = Store
		fields = ['title','logo','description',]
	

class ProductForm(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True,
    }))

    class Meta:
        model = Product
        fields = ["title", "slug", "category", "main_image", "price","inventory","description","warranty", "return_policy"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique slug here..."
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Entre price of the product..."
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description of the product...",
                "rows": 5
            }),
			"inventory": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter inventory..."
            }),
            "warranty": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product warranty here..."
            }),
            "return_policy": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product return policy here..."
            }),

        }