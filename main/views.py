from django.db.models import Q
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Post, Saved, Likes, Rating
from .serializers import PostSerializer, SavedSerializer, LikeSerializer, CreateRatingSerializer


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, ]
        else:
            permissions = []
        return [permission() for permission in permissions]


class PostViewSet(PermissionMixin, ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = Post.objects.all()
        queryset = queryset.filter(Q(name__icontains=q))
        serializers = PostSerializer(queryset, many=True,
                                    context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class LikesView(PermissionMixin, ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer

    @action(detail=False, methods=['get'])
    def favorite(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(author=request.user)
        serializer = LikeSerializer(queryset, many=True,
                                    context={'request': request})
        return Response(serializer.data, status=200)


class SavedView(generics.ListCreateAPIView):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer
    permission_classes = [IsAuthenticated]


class AddStarRatingView(PermissionMixin, ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

