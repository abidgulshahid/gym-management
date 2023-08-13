from django.urls import path
from gym_users.views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
]

