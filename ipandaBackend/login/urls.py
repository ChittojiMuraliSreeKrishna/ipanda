from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('register/', views.registrationPage, name="User Registration")
]
