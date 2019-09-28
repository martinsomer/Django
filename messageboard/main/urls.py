from . import views
from django.urls import path, include

urlpatterns = [
    path('new/', views.create_thread, name = 'create_thread'),
]
