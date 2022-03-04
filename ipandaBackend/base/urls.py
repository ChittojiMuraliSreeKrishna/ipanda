from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.getRoutes, name='get urls'),
    path('user/', include('urm.urls')),
    path('accounting/', include('accounting.urls')),
    path('billing/', include('billing.urls')),
    path('inventory/', include('inventory.urls')),
    path('reports/', include('reports.urls'))
]
