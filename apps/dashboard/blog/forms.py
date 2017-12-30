from django import forms

from apps.blog import models


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ('date_added',)
