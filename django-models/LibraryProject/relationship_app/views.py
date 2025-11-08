from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Class-based view to list all libraries
class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'

# User Registration View (keep as function-based)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('relationship_app:list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom Login View that extends Django's LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    
    def form_valid(self, form):
        messages.info(self.request, f'You are now logged in as {form.get_user().username}.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

# Custom Logout View that extends Django's LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You have successfully logged out.')
        return super().dispatch(request, *args, **kwargs)
