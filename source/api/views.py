from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from api.permissions import PermissionPost, PermissionAddLikeDelete
from api.serializers import PostSerializer, CommentSerializer, LikeSerializer
from posts.models import Post, Comment, Like


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PermissionPost, ]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()


class LikeView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, PermissionAddLikeDelete]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def delete(self, request, pk):
        self.destroy()


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()
