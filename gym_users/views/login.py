from django.shortcuts import render
from django.views import View

from gym_users.forms.login import UserLoginForm


class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'gym_users/login.html', context=context)
