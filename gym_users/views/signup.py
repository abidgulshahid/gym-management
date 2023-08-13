from django.shortcuts import render
from django.views import View

from gym_users.forms.signup import UserSignUpForm


class SignUpView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserSignUpForm()
        context = {'form': form}
        return render(request, 'gym_users/signup.html', context=context)
