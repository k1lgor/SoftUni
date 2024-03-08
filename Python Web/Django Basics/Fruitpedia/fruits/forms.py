from django import forms

from .models import Fruit


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ("name", "image_url", "description", "nutrition")
        labels = {
            "name": "",
            "image_url": "",
            "description": "",
            "nutrition": "",
        }
        error_messages = {
            "fruit_name": {
                "unique": "This fruit name is already in use! Try a new one.",
            }
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Fruit Name"}),
            "image_url": forms.URLInput(attrs={"placeholder": "Image URL"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "nutrition": forms.Textarea(attrs={"placeholder": "Nutrition Info"}),
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ("owner",)


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ("name", "image_url", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = "readonly"
            field.widget.attrs["disabled"] = "disabled"
