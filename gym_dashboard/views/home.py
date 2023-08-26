from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class Dashboard(View):
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        print(request.user.type)
        if request.user.is_authenticated: return render(request, 'gym_dashboard/dashboard.html', context={'request':request})
        return HttpResponseRedirect(reverse_lazy('index_view'))
