from django.urls import path
from .views import DashboardView,WaterStateView


urlpatterns = [
    path('',DashboardView.as_view()),
    path('waterstate/',WaterStateView.as_view())
]