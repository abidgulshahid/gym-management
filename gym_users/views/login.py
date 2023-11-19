from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import login, authenticate
from gym_users.forms.login import UserLoginForm
from gym_users.models import ScheduleClass


class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        '''
        if the user is logged in and their type is USER then it will redirect to user dashboard or 
        it will redirect to coach dashboard... if the user is not logged in it will redirect to login page
        '''

        if request.user.is_authenticated and request.user.type == 'user':
            if 'get_list' in request.GET:
                print('here')
                current_classes = ScheduleClass.objects.filter(user_id=request.user.id)
                context = {'class': current_classes}
                string = render(request, 'gym_dashboard/_partial/_list.html', context=context)
                return HttpResponse(string)

            return render(request, 'gym_dashboard/dashboard.html', context={'request': request, 'form': form})
        elif request.user.is_authenticated and request.user.type == 'coach':
            admin_url = reverse('admin:index')
            return redirect(admin_url)
        return render(request, 'gym_users/login.html', context=context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():

            data = form.cleaned_data
            user = authenticate(**data)
            # this line take username password if it found in our db then it will redirect it to dashboard
            if user:
                if user.type == "TRAINER":
                    login(request, user)
                    admin_url = reverse('admin:index')
                    return redirect(admin_url)
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('dashboard_view'))
            context = {'form': form, 'message': "Email Doesn't Exist"}
            return render(request, 'gym_users/login.html', context=context)
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, 'gym_users/login.html', context=context)