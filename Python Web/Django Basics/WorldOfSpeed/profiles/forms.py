from django import forms

from profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")
        widgets = {
            "password": forms.PasswordInput(),
        }

        help_texts = {
            "age": "Age requirement: 21 years and above.",
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("owner",)
        widgets = {
            "password": forms.PasswordInput(),
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = "readonly"
