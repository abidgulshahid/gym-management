from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login, authenticate
from gym_users.forms.signup import UserSignUpForm
from gym_users.models import User


class SignUpView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserSignUpForm()
        context = {'form': form}
        return render(request, 'gym_users/signup.html', context=context)

    def post(self, request):
        form = UserSignUpForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            email = data['email']
            password = data['password']
            type = data['type']
            User.objects.create(
                email = email,
                username= email,
                type= type,
                password= password
            )
            return HttpResponseRedirect(reverse_lazy('login_view'))
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, 'gym_users/signup.html', context=context)