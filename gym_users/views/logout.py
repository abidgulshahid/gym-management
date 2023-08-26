from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login, authenticate
from gym_users.forms.login import UserLoginForm


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('index_view'))