from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import profile

class UserRegisterForm(UserCreationForm):  # user register inherit UserCreationForm
    email = forms.EmailField()
    class Meta:
           model = User
           fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm): # user register update
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    class Meta():
        model = User
        fields = ['username','email','first_name','last_name']

class ProfileUpdateForm (forms.ModelForm): # profile image adding
    present_address = forms.CharField(label='Present Addres')
    perment_address = forms.CharField(label='perment Addres')
    bio = forms.CharField(label='Bio')
    birthday =forms.DateField()
    contact =forms.CharField(label='contact')
    class Meta:
        model = profile
        fields = ['present_address','perment_address','bio','birthday','image','contact']
        """widgets = {
            'birthday': DateInput(),
        }"""

#class DateInput(forms.DateInput):
     #input_type = 'date'
    
"""class profileUpdateForms(forms.ModelForm): # profile extra fields adding when profile updatings
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    present_address = forms.CharField(label='Present Addres')
    perment_address = forms.CharField(label='perment Addres')
    bio = forms.CharField(label='Bio')
    birthday =forms.DateField()
    contact =forms.CharField(label='contact')
    class Meta():
        model = profile 
        fields = ['first_name','last_name','present_address','perment_address','bio','birthday','image']
        widgets = {
            'birthday': DateInput(),
        }
        """
