from django import forms

from .models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "password")
        help_text = {
            "password": "*Password length requirements: 8 to 20 characters",
        }
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": "",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Password"},
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "image_url", "age")

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "image_url": "Image URL",
            "age": "Age",
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
