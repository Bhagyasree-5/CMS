from django import forms 
from .models import *

class ChemicalForm(forms.ModelForm):
    class Meta:
        model = Chemicals
        fields = '__all__'


class addUtensilForm(forms.ModelForm):
    class Meta:
        model = Utensils
        fields = '__all__'

class FineForm(forms.ModelForm):
    class Meta:
        model = Fine
        exclude = ['price']
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchasedDetails
        fields = '__all__'  # Use all fields from the model, or specify a list of fields
        widgets = {
            'chem_name': forms.Select(attrs={'class': 'form-control'}),
            'Purchased_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Bill_no':forms.TextInput(attrs={'class': 'form-control'}),
            'Rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'Quantity_purchased': forms.NumberInput(attrs={'class': 'form-control'}),
            'Balance': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }