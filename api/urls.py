
from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('', views.getRoutes),
    path('meals/', views.getMeals),
    path('meals/<str:pk>', views.getMeal),
    path('profiles/', views.getProfiles),
    path('profiles/<str:pk>', views.getProfile),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
