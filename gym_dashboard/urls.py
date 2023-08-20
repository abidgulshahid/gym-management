from django.urls import path
from gym_dashboard.views.home import Dashboard

urlpatterns = [
    path('',Dashboard.as_view(), name='dashboard_view')
]