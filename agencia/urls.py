from django.urls import path

from agencia import views

urlpatterns = [
    path('marca/', views.MarcaViews.as_view(), name='marca'),
    path('auto/', views.AutoViews.as_view(), name='auto'),
    path('inventario/', views.InventarioViews.as_view(), name='inventario'),
    path('ventas/', views.VentasViews.as_view(), name='ventas'),
]