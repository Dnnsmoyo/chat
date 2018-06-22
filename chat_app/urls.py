"""chat_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from chat import views

urlpatterns = [
    url(r'^$', views.BroadcastChatView.as_view(), name='broadcast_chat'),
    url(r'^userchat/$', views.UserChatView.as_view(), name='user_chat'),
    url(r'^groupchat/$', views.GroupChatView.as_view(), name='group_chat'),
    url(r'^signup',views.SignupView.as_view(),name='signup'),
    url(r'^login',views.LoginView.as_view(),name='login'),
    url(r'^logout',views.LogoutView.as_view(),name='logout'),
    url(r'^new-profile/$',views.ProfileFormView.as_view(),name='profile_form'),
    url(r'^profile/(?P<pk>\d+)$',views.ProfileDetailView.as_view(),name='profile_detail'),
    url(r'^new-group/$',views.GroupFormView.as_view(),name='group_form'),
    url(r'^group/(?P<pk>\d+)$',views.GroupDetailView.as_view(),name='group_detail'),
    url(r'^add_user$',views.add_user,name='add_user'),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
]
