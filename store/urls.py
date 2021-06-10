from django.urls import path
from store.views import *

urlpatterns = [
    path("",ProductView.as_view()),
    path("<int:product_id>/",ProductDetailView.as_view()),
    path('signup/',CustomerSignUpView.as_view()),
    path('login/',CustomerLoginView.as_view()),
    path("categories/",CategoryView.as_view()),
    path("cart/",CartIndexView.as_view()),
    path('orders/',OrderIndexView.as_view()),
    path("logout/",CustomerLogoutView.as_view()),
    path('is-auth/',IsAuthencatedCustomer.as_view()),
]