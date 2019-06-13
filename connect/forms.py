from .models import Foundation, Awareness, Forums, Profile, Comment
from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Forums
        exclude = ['post_date', 'post_user']

class NewCommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['comment_id', 'user_comment']