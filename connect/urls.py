from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^foundations/',views.foundation,name='foundation'),
    url(r'^search/',views.search_results,name='search'),
    url(r'^api/foundations/$', views.FoundationList.as_view()),
    url(r'^api/awareness/$', views.AwarenessList.as_view()),
    url(r'^api/forums/$', views.ForumsList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/comments/$', views.CommentList.as_view()),
    url(r'^forums/',views.forums, name ='forums'),
    url(r'^awareness/',views.awareness, name ='awareness'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^solution/(\d+)/', views.comment, name = 'comment'),
    url(r'^profile/$',views.profile,name = 'NewProfile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit_profile/$',views.edit_profile,name = 'edit_profile'),
    url(r'^tests/',views.tests, name ='tests'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
