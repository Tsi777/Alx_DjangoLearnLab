from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import CustomLoginView, CustomLogoutView

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: List all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view: List all libraries
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),
    
    # Class-based view: Show details for a specific library
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views - Using Django's built-in views with custom templates
    path('register/', views.register_view, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]