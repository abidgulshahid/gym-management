from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login, authenticate
from gym_users.forms.login import UserLoginForm


class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'gym_users/login.html', context=context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(**data)
            print(user, 'user')
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('dashboard_view'))
            context = {'form': form}
            return render(request, 'gym_users/login.html', context=context)
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, 'gym_users/login.html', context=context)
