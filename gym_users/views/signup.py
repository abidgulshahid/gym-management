
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from gym_users.forms.signup import UserSignUpForm


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
        '''if USER/COACH fill their form correctly then first it save the form, save the password in 
        encrypted form then if type is coach then assign it to staff category else normal category'''
        if form.is_valid():
            data = form.cleaned_data
            user = form.save(commit=False)
            type = data['type']
            print(data['email'])
            user.username = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']

            user = form.save()
            user.set_password(user.password)
            if type == 'coach':
                user.is_staff= True
            else:
                user.is_staff = False
            user.is_active = True
            user.save()
            user.refresh_from_db()
            user.profile.father_name = data['father_name']
            user.profile.birth_date = data['birth_date']
            user.profile.cnic = data['cnic']
            user.profile.address = data['address']
            user.profile.experience = data['experience']
            user.profile.gym_time = data['gym_time']
            user.profile.memebership_date = data['memebership_date']
            user.profile.mobile_no = data['mobile_no']
            user.save()
            auth = authenticate(**data)
            if auth:
                if user.type == "coach":
                    login(request, auth)
                    admin_url = reverse('admin:index')
                    return redirect(admin_url)
                login(request, auth)
                return HttpResponseRedirect(reverse_lazy('dashboard_view'))
            return HttpResponseRedirect(reverse_lazy('login_view'))
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, 'gym_users/signup.html', context=context)
