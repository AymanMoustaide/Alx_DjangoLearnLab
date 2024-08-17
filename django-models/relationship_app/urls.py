from django.contrib import admin
from django.urls import path
from relationship_app import views
from relationship_app.views import LibraryDetailView
from .views import list_books
from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('books/', list_books, name='list_books'),
    path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', UserRegisterView.as_view(template_name='relationship_app/register.html'), name='views.register'),
    path('admin/', admin_view, name='admin'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),]

'''from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # Add other URL patterns here
]


from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('bedit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    # Other URL patterns...
]'''