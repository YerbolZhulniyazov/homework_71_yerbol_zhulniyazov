from django.urls import path
from posts.views import HomePostView, PostAddView, PostsDetailView, CommentAddView, add_like, PostUpdateView, \
    PostDeleteView

urlpatterns = [
    path('', HomePostView.as_view(), name='index'),
    path('posts/add', PostAddView.as_view(), name='posts_add'),
    path('post/detail/<int:pk>', PostsDetailView.as_view(), name='posts_detail'),
    path('post/add/comment/<int:pk>', CommentAddView.as_view(), name='to_comment'),
    path('post/like/<int:pk>', add_like, name='like_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/confirm-delete/', PostDeleteView.as_view(), name='confirm_delete'),
    ]
