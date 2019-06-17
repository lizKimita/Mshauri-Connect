from .models import Foundation, Awareness, Forums, Profile, Comment,Assessment
from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Forums
        exclude = ['post_date', 'post_user']

class NewCommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['comment_id', 'user_comment']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']

class NewYesAssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        exclude = ['user','yesscore','noscore','date']

class NewNoAssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        exclude = ['user','yesscore','noscore','date']

