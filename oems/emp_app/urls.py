from django.urls import path
from .views import employee

urlpatterns =[
    path('emp/', employee),
 ]