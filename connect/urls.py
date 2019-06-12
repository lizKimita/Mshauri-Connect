from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^api/foundations/$', views.FoundationList.as_view()),
    url(r'^api/awareness/$', views.AwarenessList.as_view()),
    url(r'^api/forums/$', views.ForumsList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/comments/$', views.CommentList.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)