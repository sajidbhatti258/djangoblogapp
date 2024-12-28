from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Comment, Post  # Ensure you have the correct imports

class CommentsCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment/comment_form.html'
    fields = ['content']
    login_url = 'users:login'  # Redirect to login if the user is not authenticated

    def form_valid(self, form):
        # Automatically associate the comment with the related post
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        form.instance.post = post

        # Associate the logged-in user with the author field
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the post detail page after successful comment submission
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return reverse('blog:post_detail', kwargs={'pk': post.pk, 'slug': post.slug})

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comment/comment_form.html'
    fields = ['content']
    login_url = 'users:login'  # Redirect to login if the user is not authenticated

    def get_object(self):
        # Retrieve the comment using pk and ensure it belongs to the logged-in user
        pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=pk, author=self.request.user)
        return comment

    def get_success_url(self):
        # Redirect back to the post detail view of the associated post
        post_pk = self.object.post.pk  # Get the related post's pk
        post_slug = self.object.post.slug  # Get the related post's slug
        return reverse_lazy('blog:post_detail', kwargs={'pk': post_pk, 'slug': post_slug})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment/comment_confirm_delete.html'  # Replace with your actual template
    login_url = 'users:login'  # Redirect to login if the user is not authenticated

    def get_object(self):
        # Retrieve the comment object
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])

        # Check if the comment belongs to the current user
        if comment.author != self.request.user:
            raise PermissionDenied("You are not allowed to delete this comment.")
        
        return comment

    def get_success_url(self):
        # Redirect to the post detail page after deletion
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk, 'slug': self.object.post.slug})
