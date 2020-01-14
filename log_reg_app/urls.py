from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg', views.reg),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),

]