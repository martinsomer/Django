from . import views
from django.urls import path, include

urlpatterns = [
    path('new/', views.create_thread, name = 'create_thread'),
    path('', views.index, name = 'index'),
    path('view/<int:id>/', views.view_thread, name = 'view_thread'),
]
