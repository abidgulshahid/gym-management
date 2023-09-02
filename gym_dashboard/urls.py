from django.urls import path
from gym_dashboard.views.home import Dashboard
from gym_dashboard.views.settings import SettingView

urlpatterns = [
    path('',Dashboard.as_view(), name='dashboard_view'),
    path('settings/',SettingView.as_view(), name='settings_view')
]