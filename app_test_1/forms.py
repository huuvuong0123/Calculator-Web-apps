from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label="Number 1")
    num2 = forms.FloatField(label="Number 2")
    operation = forms.ChoiceField(choices=[('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide')])
    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')