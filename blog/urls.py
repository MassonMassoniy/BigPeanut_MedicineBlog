from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register('post', PostUpdateView, basename = 'post_api')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('', home_view, name='home-view'),
    path('post/new/', post_page, name='post_page'),
    path('post/<int:pk>/', post_view, name='post'),
    
    path('post/update/', PostUpdateView.as_view({'patch':'update'})),
    path('post/comment/api/create/', CommentView.as_view({'post':'create'})),
    path('post/list/', PostView.as_view({'get':'list'})),
    path('post/create/', PostView.as_view({'post':'create'})),
]