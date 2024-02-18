from django import forms

from .models import Album


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        labels = {
            "album_name": "Album Name",
        }
        widgets = {
            "album_name": forms.TextInput(attrs={"placeholder": "Album Name"}),
            "artist": forms.TextInput(attrs={"placeholder": "Artist"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "image_url": forms.URLInput(attrs={"placeholder": "Image URL"}),
            "price": forms.NumberInput(attrs={"placeholder": "Price"}),
        }


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
