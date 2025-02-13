from django.urls import path
from .views import index, about, contact, portfoliopage  # 

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('portfoliopage/', portfoliopage, name='portfoliopage'),  
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
