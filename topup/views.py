from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopUpOrderSerializer
from django.utils import timezone
from django.db.models import Count, Sum
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from collections import defaultdict
from datetime import timedelta
from .models import TopUpOrder

class TopUpOrderCreateView(APIView):
  def post(self, request):
    serializer = TopUpOrderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Top-up order created successfully!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@staff_member_required
def analytics_dashboard(request):
  today = timezone.now().date()
  start_date = today - timedelta(days=6)

  # 1. Top 5 Most Purchased Top-Up Products
  top_products = (
      TopUpOrder.objects.filter(status='success')
      .values('product__name')
      .annotate(purchase_count=Count('id'))
      .order_by('-purchase_count')[:5]
  )

  # 2. Daily Revenue (last 7 days)
  daily_revenue = (
      TopUpOrder.objects.filter(status='success', created_at__date__gte=start_date)
      .values('created_at__date')
      .annotate(total_revenue=Sum('product__price'))
      .order_by('created_at__date')
  )

  # Format revenue for easier display
  revenue_map = defaultdict(lambda: 0)
  for entry in daily_revenue:
      revenue_map[entry['created_at__date']] = entry['total_revenue']

  revenue_data = [
      {'date': (today - timedelta(days=i)), 'revenue': revenue_map[today - timedelta(days=i)]}
      for i in range(6, -1, -1)
  ]

  # 3. Failed Payments (current month)
  current_month = today.month
  current_year = today.year
  failed_payments = TopUpOrder.objects.filter(
      status='failed',
      created_at__year=current_year,
      created_at__month=current_month
  ).count()

  context = {
      'top_products': top_products,
      'revenue_data': revenue_data,
      'failed_payments': failed_payments
  }

  return render(request, 'topup/dashboard.html', context)

