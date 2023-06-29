from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register('user', UserUpdateView, basename = 'user_updater')
#router.register('country', CountryView, basename = 'country_viewer')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('token/get/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('user/api/country/create/', CountryCreateView.as_view({'post': 'create'})),
    path('user/api/country/update/<int:pk>/', CountryUpdateView.as_view({'put': 'update'})),

    path('user/api/register/', RegisterView.as_view({'post': 'create'})),
    path('user/api/profile/', UserView.as_view({'get': 'get_current_user'})),

    path('user/profile/', profile, name='Profile'),
    path('user/login/', login, name='Login'),
    path('user/register/', register, name='Registration'),
    path('user/profile/password_update/', password_update_page, name='Password_update'),
]
