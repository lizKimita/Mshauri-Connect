from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Foundation, Awareness, Forums, Profile, Comment
from .serializer import FoundationSerializer, AwarenessSerializer, ForumsSerializer, ProfileSerializer, CommentSerializer
from .forms import NewPostForm, NewCommentsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from rest_framework import status

# Create your views here.
def home(request):
    return render(request,'index.html')


class FoundationList(APIView):
    def get(self,request,format=None):
        all_foundations = Foundation.objects.all()
        serializers = FoundationSerializer(all_foundations,many=True)
        return Response(serializers.data)
    def post(self,request,format=None):
        serializers = FoundationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
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
        return redirect('forums')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def comment(request,id):
    post = Forums.objects.filter(id=id)
    current_user = request.user

    if request.method=='POST':
        form = NewCommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_comment = request.user
            form.comment_id = id
            form.save()
            return redirect('comment',id)
    else:
        form=NewCommentsForm()
    user_solution=Comment.objects.filter(comment_id=id)
    try:
        pass
    except Exception as e:
        raise Http404()
   
    return render(request, 'comment.html',{'post':post, 'current_user': current_user,  'form':form, 'comments':user_solution})
