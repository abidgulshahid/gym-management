from django.contrib import admin
from gym_users.models import User, Payments, ScheduleClass, ContactForm, Profile, Equipment


# Register your models here.


class ScheduleClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ScheduleClass._meta.get_fields()]


class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payments._meta.get_fields()]


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'type', 'created_at']
    search_fields = ['type', 'username']


class EquimentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipment._meta.get_fields()]


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]


class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactForm._meta.get_fields()]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Equipment, EquimentAdmin)
admin.site.register(Payments, PaymentAdmin)
admin.site.register(ScheduleClass, ScheduleClassAdmin)
admin.site.register(ContactForm, ContactAdmin)
admin.site.register(User ,UserAdmin)