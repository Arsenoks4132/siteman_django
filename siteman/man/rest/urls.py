from django.urls import path, re_path, include

from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'man', views.ManViewSet)

urlpatterns = [
    # path('api/v1/', include(router.urls))
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/men/', views.ManAPIList.as_view()),
    path('api/v1/men/<int:pk>/', views.ManAPIUpdate.as_view()),
    path('api/v1/mendelete/<int:pk>/', views.ManAPIDestroy.as_view()),
]
