from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('checkout/<int:item_id>/', views.checkout, name='checkout'),
]