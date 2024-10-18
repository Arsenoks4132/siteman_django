from django.urls import path, re_path

from . import views

urlpatterns = [
    path('api/v1/manlist/', views.ManAPIList.as_view()),
    path('api/v1/manlist/<int:pk>/', views.ManAPIUpdate.as_view()),
    path('api/v1/mandetail/<int:pk>/', views.ManAPIDetailView.as_view()),
]
