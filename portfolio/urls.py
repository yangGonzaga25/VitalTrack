from django.urls import path
from .views import index, about, contact, portfoliopage, activity2_dashboard, reports, inventory

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('portfoliopage/', portfoliopage, name='portfoliopage'),  
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('activity2/', activity2_dashboard, name='activity2_dashboard'),
    path('reports/', reports, name='reports'),
    path('inventory/', inventory, name='inventory'), 
]
