#Tanya Grace S. Gonzaga - Activity3

from django.urls import path
from .views import add_medicine, delete_medicine, get_medicine, get_medicines, update_medicine

app_name = "items"

urlpatterns = [
    path('', get_medicines, name='get_medicines'),
    path('<int:medicine_id>/', get_medicine, name='get_medicine'),
    path('add/', add_medicine, name='add_medicine'),
    path('update/<int:medicine_id>/', update_medicine, name='update_medicine'),
    path('delete/<int:medicine_id>/', delete_medicine, name='delete_medicine'),
]

