from django import forms

from cars.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")
        exclude = ("owner",)
        widgets = {
            "image_url": forms.URLInput(attrs={"placeholder": "https://..."}),
        }
        error_messages = {
            "image_url": {
                "unique": "This image URL is already in use! Provide a new one.",
            }
        }


class EditCarForm(CreateCarForm):

    pass


class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = "readonly"
