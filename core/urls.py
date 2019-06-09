from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import index, about, contact


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('logout', LogoutView.as_view(
        template_name='logout.html'), name='logout'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
]
