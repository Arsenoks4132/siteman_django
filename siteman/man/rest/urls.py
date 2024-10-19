from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'man', views.ManViewSet)

urlpatterns = [
    # path('api/v1/', include(router.urls))
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/men/', views.ManAPIList.as_view()),
    path('api/v1/men/<int:pk>/', views.ManAPIUpdate.as_view()),
    path('api/v1/mendelete/<int:pk>/', views.ManAPIDestroy.as_view()),

    path(r'api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
