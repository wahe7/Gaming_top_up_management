from django.urls import path
from .views import TopUpOrderCreateView, analytics_dashboard

urlpatterns = [
    path('api/topup/', TopUpOrderCreateView.as_view(), name='topup-order'),
    path('dashboard/', analytics_dashboard, name='dashboard'),
]
