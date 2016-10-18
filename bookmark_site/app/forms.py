from django import forms
from app.models import Bookmark


class BookmarkForm(forms.ModelForm):

    class Meta:
        fields = ("full_url", "title", "description")
        model = Bookmark
