from django import forms

from .models import Plant


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"


class DeletePlantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.arrts["readonly"] = "readonly"
