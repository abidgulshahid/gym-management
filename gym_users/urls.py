from django.urls import path
from gym_users.views.index import IndexView
from gym_users.views.login import LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('login/', LoginView.as_view(), name='login_view'),
]

