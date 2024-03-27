from django.urls import path
from seller import views

urlpatterns = [
    path('',views.RegisterView.as_view(), name = 'signup'),
    path('signin/',views.SignInView.as_view(), name = 'login'),
    path('profile/',views.HomeView.as_view(), name = 'profile'),
]