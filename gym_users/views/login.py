from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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
                print(dir(user))
                if user.type == "coach":
                    login(request, user)
                    admin_url = reverse('admin:index')
                    return redirect(admin_url)
                login(request,user)
                return HttpResponseRedirect(reverse_lazy('dashboard_view'))
            context = {'form': form, 'message':"Email Doesn't Exist"}
            return render(request, 'gym_users/login.html', context=context)
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, 'gym_users/login.html', context=context)
