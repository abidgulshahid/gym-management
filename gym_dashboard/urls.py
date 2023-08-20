from django.urls import path
from gym_dashboard.views.home import Dashboard

urlpatterns = [
    path('/home',Dashboard.as_view(), name='dasboard_view')
]