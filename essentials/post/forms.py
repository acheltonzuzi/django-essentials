# myapp/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "slug",
            "banner",
        ]  # Incluímos apenas os campos editáveis
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Título do Post"}
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Conteúdo do Post",
                    "rows": 5,
                }
            ),
            "slug": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Slug"}
            ),
            "banner": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }

