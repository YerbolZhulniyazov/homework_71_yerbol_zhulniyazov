from django.urls import path
from posts.views import HomePostView, PostAddView, PostsDetailView, CommentAddView, PostUpdateView, \
    PostDeleteView, PostLikeView

urlpatterns = [
    path('', HomePostView.as_view(), name='index'),
    path('posts/add', PostAddView.as_view(), name='posts_add'),
    path('post/detail/<int:pk>', PostsDetailView.as_view(), name='posts_detail'),
    path('post/add/comment/<int:pk>', CommentAddView.as_view(), name='to_comment'),
    path('posts/like/<int:pk>/', PostLikeView.as_view(), name='like'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/confirm-delete/', PostDeleteView.as_view(), name='confirm_delete'),
    ]
