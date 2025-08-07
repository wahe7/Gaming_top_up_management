from django.urls import path
from .views import TopUpOrderCreateView

urlpatterns = [
    path('api/topup/', TopUpOrderCreateView.as_view(), name='topup-order'),
]
