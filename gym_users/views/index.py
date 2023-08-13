from django.shortcuts import render
from django.views import View


class IndexView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'form': ''}
        return render(request, 'gym_users/index.html', context=context)
