from django.contrib.auth.views import LogoutView
from django.urls import path
from account.views import UserRegisterView, CustomLoginView


urlpatterns = [
    path("signup/", UserRegisterView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
