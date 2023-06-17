from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()

urlpatterns = [
    path('', index),

    path('post/api/create/', PostView.as_view({'post':'create'})),
    path('post/comment/api/create/', CommentView.as_view({'post':'create'})),
]