from django.contrib import admin
from gym_users.models import User, Payments, ScheduleClass, ContactForm
# Register your models here.


admin.site.register(User)
admin.site.register(ScheduleClass)
admin.site.register(Payments)
admin.site.register(ContactForm)