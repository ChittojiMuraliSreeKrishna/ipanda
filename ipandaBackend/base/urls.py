from django.urls import include, path

urlpatterns = [
    path('user/', include('login.urls'))
]
