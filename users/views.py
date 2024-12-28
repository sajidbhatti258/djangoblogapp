from django.shortcuts import render
from django.contrib.auth.views import LoginView as AuthLoginView
# Create your views here.from django.contrib.auth.views import LoginView as AuthLoginView

  # Customize the template path as per your project


from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django .views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import Profile  # Replace with the actual model you're using


class RegisterView(CreateView):
    template_name='user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user:login')
    
    def form_valid(self, form):
        messages.success(self.request, "Account created successfully! Please log in.")
        return super().form_valid(form)
    
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.model.objects.get(user__username=self.kwargs['username'])

