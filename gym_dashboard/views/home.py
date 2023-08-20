from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class Dashboard(View):
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.user.is_authenticated:return render(request, 'gym_dasboard/dashboard.html', context={})
        return HttpResponseRedirect(reverse_lazy('index_view'))