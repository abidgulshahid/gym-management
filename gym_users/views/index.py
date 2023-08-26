from django.shortcuts import render
from django.views import View

from gym_users.models import ScheduleClass


class IndexView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        classes = ScheduleClass.objects.all()
        context = {'form': '', 'classes': classes}
        return render(request, 'gym_users/index.html', context=context)
