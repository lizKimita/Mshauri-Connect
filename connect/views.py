from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Foundation, Awareness, Forums, Profile, Comment
from .serializer import FoundationSerializer, AwarenessSerializer, ForumsSerializer, ProfileSerializer, CommentSerializer
from .forms import NewPostForm, NewCommentsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'index.html')


class FoundationList(APIView):
    def get(self,request,format=None):
        all_foundations = Foundation.objects.all()
        serializers = FoundationSerializer(all_foundations,many=True)
        return Response(serializers.data)

class AwarenessList(APIView):
    def get(self,request,format=None):
        all_articles = Awareness.objects.all()
        serializers = AwarenessSerializer(all_articles,many=True)
        return Response(serializers.data)


class ForumsList(APIView):
    def get(self,request,format=None):
        all_forums = Forums.objects.all()
        serializers = ForumsSerializer(all_forums,many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)

class CommentList(APIView):
    def get(self,request,format=None):
        all_comments = Comment.objects.all()
        serializers = CommentSerializer(all_comments,many=True)
        return Response(serializers.data)

def forums(request):
    current_user = request.user
    posts = Forums.get_posts()
    title = "mshauri-connect"

    return render(request,'forums.html', {"title":title, "posts":posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_user = current_user
            # post.poster_id = current_user.id
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'forums.html', {"form": form})