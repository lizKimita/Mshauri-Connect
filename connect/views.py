from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Foundation, Awareness, Forums, Profile, Comment, Assessment
from .serializer import FoundationSerializer, AwarenessSerializer, ForumsSerializer, ProfileSerializer, CommentSerializer
from .forms import NewPostForm, NewCommentsForm, NewProfileForm, NewYesAssessmentForm, NewNoAssessmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    return render(request,'works.html')

# def tests(request):
#     tests = Assessment.objects.all()
#     current_user = request.user
#     try:
#         pass
#     except Exception as e:
#         raise  Http404()
#     yesscore = request.POST.get("like","")
#     noscore = request.POST.get("dislike","") 

#     if request.method=='POST':
#         form=NewYesAssessmentForm(request.POST)
#         yess = request.POST.get("bad","")
#         if yess:
#             bad=int(yess)
#             if form.is_valid:
#                 yesans=form.save(commit=False)
#                 single = Assessment.objects.filter(id = yess)
#                 count=0
#                 for i in single:
#                     count+=i.yesans
#                 total_yes=count+1
#                 Assessment.objects.filter(id=yess).update(yesscore=total_yes)
#                 return redirect('tests')

#     else:
#         forms=NewYesAssessmentForm()

#     return render(request,'tests.html',{"tests": tests})

def tests(request):
    current_user = request.user

    return render(request,'assessment.html')

def foundation(request):
    foundations = Foundation.objects.all()

    return render(request, 'foundations.html', {"foundations": foundations})


def awareness(request):
    awareness = Awareness.objects.all()

    return render(request, 'awareness.html', {"awareness": awareness})

def search_results(request):
    foundation= Foundation.objects.all()
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_foundation = Foundation.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"foundations": searched_foundation})

    else:
        message = "no foundation by that name"
        return render(request,'search.html',{"message":message})

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

    def post(self,request,format=None):
        serializers = AwarenessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ForumsList(APIView):
    def get(self,request,format=None):
        all_forums = Forums.objects.all()
        serializers = ForumsSerializer(all_forums,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = ForumsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentList(APIView):
    def get(self,request,format=None):
        all_comments = Comment.objects.all()
        serializers = CommentSerializer(all_comments,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

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


def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})


def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Profile.objects.get(username=request.user)
        form = NewProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request,'edit_profile.html',{'form':form})

def profile(request):
    current_user = request.user
    posts = Forums.objects.filter(post_user = current_user)

    try:
        profile = Profile.objects.get(username=current_user)
        user = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profile':profile,'current_user':current_user,'posts':posts})


def get_data(request):
    print("something")
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        message = phone_number+" is sending KES"+amount+" to you."
        return render(request, 'data.html', {"message":message})

    else:
        print("Enter something")

    return render(request, 'data.html')
