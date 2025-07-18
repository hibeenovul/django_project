from django import forms
from .models import UserProfile
from django_select2.forms import Select2Widget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.widgets import TextInput



class UserProfileForm(forms.ModelForm):
    phone_number = PhoneNumberField(
            widget=forms.TextInput(attrs={'placeholder': '+2348012345678'})
        )
        
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'country': Select2Widget
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))