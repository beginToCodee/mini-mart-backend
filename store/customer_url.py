from django.urls import path
from store.views import *

urlpatterns = [
   
    path('signup/',CustomerSignUpView.as_view()),
    path('login/',CustomerLoginView.as_view()),
    path("logout/",CustomerLogoutView.as_view()),
    path('is-auth/',IsAuthencatedCustomer.as_view()),
]