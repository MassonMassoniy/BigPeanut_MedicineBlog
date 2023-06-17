from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsADoctor

# Create your views here.

def index(request):
    ls = Post.objects.all()
    return render(request, 'index.html', {'posts_list':ls})


class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description', 'text']
    #permission_classes=[IsAuthenticated, IsNewsEditor]

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsADoctor]
        return super(self.__class__, self).get_permissions()
    

class CommentView(ModelViewSet):
    permission_classes=[AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['text']