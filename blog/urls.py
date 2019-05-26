from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('post/<int:post_id>/', views.detail, name = 'detail'),
]