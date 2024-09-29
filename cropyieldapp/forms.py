import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms import DateInput

from .models import Farmer, Login, Officer, upload_img, Announcement, Feedback


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2=forms.CharField(widget=forms.PasswordInput,label='confirm password')

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Add your custom username validation logic here
        # For example, check if the username already exists in the database
        if Login.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data
class FarmerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Farmer
        fields = ('name', 'contact_no', 'email', 'address','photo','Aadhaar_id')



    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Add your custom name validation logic here
        # For example, check if the name contains only letters and spaces
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError('Name can only contain letters and spaces.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Validate email using Django's built-in email validator
        validate_email(email)
        return email

    def clean_address(self):
        address = self.cleaned_data.get('address')
        # Add your custom address validation logic here
        # For example, check if the address is not empty
        if not address.strip():
            raise forms.ValidationError('Address cannot be empty.')
        return address

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        # Add your custom photo validation logic here
        # For example, check if the photo file size is within a certain limit
        # You can use the 'PIL' library to check image dimensions, etc.
        # This example only checks if the file size is less than 5MB
        if photo and photo.size > 5 * 1024 * 1024:
            raise forms.ValidationError('File size must be less than 5MB.')
        return photo




class OfficerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Officer
        fields = ('name', 'contact_no', 'email', 'address','office_location','office_name','photo','id_card')



class upload_form(forms.ModelForm):

    class Meta:
        model=upload_img
        fields=['img_upload']





class Announcementform(forms.ModelForm):
    class Meta:
        model=Announcement
        fields=['content']

class   FeedbackForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
    )
    class Meta:
        model = Feedback
        fields = ('subject', 'Enquiry', 'date')