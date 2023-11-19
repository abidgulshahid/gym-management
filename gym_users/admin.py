from django.contrib import admin
from gym_users.models import User, Payments, ScheduleClass, ContactForm, Profile, Equipment
# Register your models here.


admin.site.register(User)
admin.site.register(ContactForm)
admin.site.register(Profile)
admin.site.register(Equipment)

@admin.register(Payments)
class PaymentForm(admin.ModelAdmin):
    readonly_fields = ('created_at', )


class ScheduleClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ScheduleClass._meta.get_fields()]


admin.site.register(ScheduleClass, ScheduleClassAdmin)