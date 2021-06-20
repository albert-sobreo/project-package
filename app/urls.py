from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TestView),
    path('nav/', views.TestNavView),
    path('inventory/', views.InventoryView),
    path('sales/', views.SalesView),
    path('order', views.OrderView),
    path('neko/', views.NekoView),
    path('request/', views.RequestView),
    path('report', views.ReportView),
    path('reportlist', views.ReportlistView)
]