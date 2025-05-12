from django.urls import path
from .views import MyOrdersView

urlpatterns = [
    path('my_orders', MyOrdersView.as_view(), name='orders'),
]