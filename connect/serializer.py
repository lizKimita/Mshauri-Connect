from rest_framework import serializers
from .models import Foundation, Awareness, Forums, Profile, Comment


class FoundationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Foundation
        fields=('image','name','location', 'contact', 'website_link', 'description')

class AwarenessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Awareness
        fields=('article_title','article','date', 'foundation')

class ForumsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Forums
        fields=('forum_title','forum_post','post_date','post_user')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('username','tel_no','email','user_location')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('user_comment','comment','comment_id')
