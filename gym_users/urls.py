from django.urls import path
from gym_users.views.index import IndexView
from gym_users.views.login import LoginView
from gym_users.views.signup import SignUpView, SuccessMessage
from gym_users.views.logout import LogoutView
from gym_users.views.contact import ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('success/', SuccessMessage.as_view(), name='success_view')
]
