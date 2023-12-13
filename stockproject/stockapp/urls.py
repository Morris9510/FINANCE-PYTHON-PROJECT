# This code is defining the URL patterns for a Django application.
from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.stock_analysis, name='stock_analysis'),  # This points to stock_analysis view
]
