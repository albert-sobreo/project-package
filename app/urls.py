from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TestView),
    path('nav/', views.TestNavView),
    path('inventory/', views.InventoryView)
]