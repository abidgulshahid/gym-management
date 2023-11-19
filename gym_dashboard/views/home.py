from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect

from gym_dashboard.forms.payment import PaymentForm
from gym_users.models import ScheduleClass, Equipment


class Dashboard(View):
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = PaymentForm()
        print(request.user.type)
        if request.user.is_authenticated and request.user.type == 'user':
            if 'get_list' in request.GET:
                print('here')
                current_classes = ScheduleClass.objects.all()
                equipment = Equipment.objects.all()

                context = {'class': current_classes, 'equipment':equipment}
                string = render(request, 'gym_dashboard/_partial/_list.html', context=context)
                return HttpResponse(string)

            return render(request, 'gym_dashboard/dashboard.html', context={'request':request, 'form':form})
        elif request.user.is_authenticated and request.user.type == 'coach':
            admin_url = reverse('admin:index')
            return redirect(admin_url)

        return HttpResponseRedirect(reverse_lazy('index_view'))

    def post(self, request):
        print(request.POST)
        form = PaymentForm(data=request.POST)
        if 'create_entry' in request.POST:
            if form.is_valid():
                data = form.save(commit=False)
                data.user_id = request.user.id
                data.save()
                return HttpResponse("success")
