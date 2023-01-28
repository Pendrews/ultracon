from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Beneficiary


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2',]


class U_UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class P_UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['other_names', 'dob', 'gender', 'country', 'country_of_birth', 'place_of_birth',
                  'phone', 'alt_phone','dig_address', 'postal_address', 'res_address', 'ssnit',
                  'national_id', 'nok', 'nok_phone', 'nok_rel', 'nok_address','father_name', 'father_address', 'mother_name', 'mother_address','profil_pic']


class CreateBene(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['first_name','last_name', 'allocation', 'relationship', 'address', 'contact']