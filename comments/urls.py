
from django.urls import path
from .views import CommentsCreateView,CommentDeleteView, CommentUpdateView

app_name='comments'

urlpatterns = [
   path('comment/add/<int:post_id>/', CommentsCreateView.as_view(), name='comment_add'),
   path('comment/edit/<int:pk>/', CommentUpdateView.as_view(), name='edit_comment'),
   path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
