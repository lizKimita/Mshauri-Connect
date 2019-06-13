from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Foundation, Awareness, Forums, Profile, Comment
from .serializer import FoundationSerializer, AwarenessSerializer, ForumsSerializer, ProfileSerializer, CommentSerializer


# Create your views here.
def home(request):
    return render(request,'index.html')


def foundation(request):

    foundations = Foundation.objects.all()

    return render(request, 'foundations.html', {"foundations": foundations})

def search_results(request):
    foundation= Foundation.objects.all()
    if 'foundation' in request.GET and request.GET["foundation"]:
        search_term = request.GET.get("foundation")
        searched_foundation = (search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"foundation":foundation})

    else:
        message = "no foundation by that name"
        return render(request,'search.html',{"message":message})    

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