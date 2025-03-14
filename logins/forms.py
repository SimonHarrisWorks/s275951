from django import forms
from .models import customer
# basic imports to access and add data into the table customer

# when the form is handed in it uses the set varibles example: CFirstname to assign the input data as the correct names into customer table
class customerSignup(forms.ModelForm):
    class Meta:
        model=customer
        fields=["CFirstName","CUsername","CEmail","CPassword"]