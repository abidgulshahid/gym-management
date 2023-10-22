from django.shortcuts import render
from django.views import View
from gym_users.forms.contact import Contact
from gym_users.models import ContactForm


class ContactView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(ContactView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = Contact()
        context = {'form': form}
        return render(request, 'gym_users/contact.html', context=context)

    def post(self,request):
        form = Contact(data=request.POST)
        if form.is_valid():
            print('saved')
            form.save()
            return render(request, 'gym_users/success.html', context={"message":"Message Sent Successfully"})
        context = {'form': form}
        print(form.errors)
        return render(request, 'gym_users/contact.html', context=context)
