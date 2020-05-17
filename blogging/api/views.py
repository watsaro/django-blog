from rest_framework import viewsets, mixins
from rest_framework import permissions
from blogging.api.serializers import PostSerializer
from blogging.models import Post

class PostViewSet(
        viewsets.GenericViewSet,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        mixins.CreateModelMixin
                  ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [] #[permissions.IsAuthenticated]