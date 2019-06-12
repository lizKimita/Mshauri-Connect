from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Foundation, Awareness, Forums, Profile, Comment
from .serializer import FoundationSerializer, AwarenessSerializer, ForumsSerializer, ProfileSerializer, CommentSerializer


# Create your views here.
def home(request):
    return render(request,'index.html')


def hoods(request):

    foundations = Foundation.objects.all()

    return render(request, 'foundation.html', {"foundations": foundations})

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