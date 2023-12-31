from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect

from gym_dashboard.forms.payment import PaymentForm
from gym_dashboard.forms.settings import SettingsForm
from gym_users.models import ScheduleClass, Profile, Payments


class SettingView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(SettingView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = PaymentForm(instance=Payments.objects.filter(user_id=request.user.id).last())
        check_payment = Payments.objects.filter(user_id=request.user.id).last()

        setting_form = SettingsForm(instance=Profile.objects.filter(user_id=request.user.id).first())
        if request.user.is_authenticated and request.user.type == 'user':
            return render(request, 'gym_dashboard/settings.html',
                          context={'request': request, 'setting_form': setting_form, 'form': form, 'check_payment':check_payment})
        elif request.user.is_authenticated and request.user.type == 'coach':
            admin_url = reverse('admin:index')
            return redirect(admin_url)

        return HttpResponseRedirect(reverse_lazy('index_view'))

    def post(self, request):
        print(request.POST)
        if 'save_setting' in request.POST:
            form = PaymentForm()
            setting_form = SettingsForm(data=request.POST, instance=Profile.objects.get(user_id=request.user.id))
            data = setting_form.save(commit=False)
            data.user_id = request.POST.get('save_setting')
            data.save()
            print('saved')
            message = "success"
            return render(request, 'gym_dashboard/settings.html',
                          context={'request': request, 'setting_form': setting_form, 'form': form, 'message':message})

        if 'save_payment' in request.POST:
            form = PaymentForm(data=request.POST)
            setting_form = SettingsForm(data=request.POST, instance=Profile.objects.get(user_id=request.user.id))
            if form.is_valid():
                data = form.save(commit=False)
                data.user_id = request.user.id
                data.save()
                return render(request, 'gym_dashboard/settings.html',
                              context={'request': request, 'setting_form': setting_form, 'form': form})