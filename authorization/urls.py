from django.contrib import admin
from django.urls import path, include
from .views import index #,RegisterView, LoginView
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    #path('register/', RegisterView.as_view(), name="register"),
    #path('login/', LoginView.as_view(), name="login"),
]
