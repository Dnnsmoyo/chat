# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from chat.models import Profile
from django.http import HttpResponse
from .forms import ProfileForm, GroupForm
from django.contrib.auth.models import User, Group
from allauth.account.views import SignupView, LoginView, LogoutView
# Create your views here.
def add_user(request):
    user = User.objects.get(username=request.user.username)
    g = Group.objects.get(name='Tech')
    users = User.objects.all()
    for u in users:
        g.user_set.add(u)
        return redirect('/')

class ProfileFormView(CreateView):
    template_name= 'profile_form.html'
    form_class = ProfileForm
    success_url ='/'
    
class ProfileDetailView(DetailView):
    #template_name='profile_detail.html'
    model = Profile

class GroupFormView(CreateView):
    template_name= 'chat/group_form.html'
    form_class = GroupForm
    success_url ='/'
    
class GroupDetailView(DetailView):
    #template_name='profile_detail.html'
    model = Group

class SignupView(SignupView):
    template_name = 'accounts/signup.html'


class LoginView(LoginView):
    template_name = 'accounts/login.html'


class LogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    
class BroadcastChatView(TemplateView):
    template_name = 'broadcast_chat.html'

    def get(self, request, *args, **kwargs):
        welcome = RedisMessage('Hello everybody')  # create a welcome message to be sent to everybody
        RedisPublisher(facility='foobar', broadcast=True).publish_message(welcome)
        return super(BroadcastChatView, self).get(request, *args, **kwargs)

    def profiles(request):
        pros = Profile.objects.get(user=request.user)
        return render(request,template_name,{'pros':pros})


class UserChatView(TemplateView):
    template_name = 'user_chat.html'

    def get_context_data(self, **kwargs):
        context = super(UserChatView, self).get_context_data(**kwargs)
        context.update(users=User.objects.all())
        return context

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UserChatView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        redis_publisher = RedisPublisher(facility='foobar', users=[request.POST.get('user')])
        message = RedisMessage(request.POST.get('message'))
        redis_publisher.publish_message(message)
        return HttpResponse('OK')


class GroupChatView(TemplateView):
    template_name = 'group_chat.html'

    def get_context_data(self, **kwargs):
        context = super(GroupChatView, self).get_context_data(**kwargs)
        context.update(groups=Group.objects.all())
        return context

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(GroupChatView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        redis_publisher = RedisPublisher(facility='foobar', groups=[request.POST.get('group')])
        message = RedisMessage(request.POST.get('message'))
        redis_publisher.publish_message(message)
        return HttpResponse('OK')
    
