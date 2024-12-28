from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Category


# Display a list of all published posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['categories'] = Category.objects.all()
       return context
    def get_queryset(self):
        # Only return published posts ordered by latest publish date
        return Post.objects.filter(is_published=True).order_by('-published_date')


# Display details of a single post, including related comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # Add comments related to the post in the context
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context


# Display posts filtered by a specific category
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Post, Category

class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        return Post.objects.filter(category=category, is_published=True).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_category_slug = self.kwargs.get('slug')
        current_category = get_object_or_404(Category, slug=current_category_slug)
        context['categories'] = Category.objects.all()
        context['current_category'] = current_category
        context['category_image'] = current_category.image.url if current_category.image else None  # Assuming Category model has an 'image' field
        return context



# Allow logged-in users to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'category', 'content', 'is_published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        # Assign the current logged-in user as the author of the post
        form.instance.author = self.request.user
        return super().form_valid(form)
