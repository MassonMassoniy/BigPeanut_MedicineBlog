from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment, Ip
from authorization.models import Country
from .serializers import PostUpdateSerializer, PostSerializer, CommentSerializer
from .permissions import IsOwner, IsADoctor, IsAdmin

# Create your views here.


def post_page(request):
    return render(request, 'post_new.html')


def post_sorted_page(request):
    posts_list = Post.objects.all()
    return render(request, 'post_sorted.html', {'posts_list':posts_list})


class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description', 'text', 'post_type']
    #permission_classes=[IsAuthenticated, IsNewsEditor]

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsADoctor]

        return super(self.__class__, self).get_permissions()


class PostUpdateView(ModelViewSet):
    permission_classes = [IsOwner|IsAdmin]
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        return super().get_permissions()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CommentView(ModelViewSet):
    #permission_classes=[IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['text']

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        
        return super(self.__class__, self).get_permissions()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'index.html', context)


def post_view(request, pk):
    post = get_object_or_404(Post.objects.all(), pk=pk)
    country = get_object_or_404(Country.objects.all(), id_id=post.user)

    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        post.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        post.views.add(Ip.objects.get(ip=ip))

    context = {
        'post' : post,
        'country' : country,
    }
    return render(request, 'post_single.html', context)