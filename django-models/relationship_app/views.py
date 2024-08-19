from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from models import Book
from forms import BookForm

# Create your views here.
def book_list_view(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

class LibraryDetails_view(DetailView):
  """A class-based view for displaying details of a specific library."""
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the library."""
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating() 


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

def LogoutView(request):
    return render(request, 'logout.html')

def LoginView(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'authentication/logout.html'

# Registration view
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')

"UserCreationForm()", "relationship_app/register.html"

def check_role(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

# Admin view
@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Add book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

# Edit book view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form})

# Delete book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})


'''from django.shortcuts import render
from .models import Book  # Assuming you have a Book model


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library  # Assuming you have a Library model

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Login view
def login_view(request):
    return auth_views.LoginView.as_view(template_name='relationship_app/login.html')(request)

# Logout view
def logout_view(request):
    return auth_views.LogoutView.as_view(template_name='relationship_app/logout.html')(request)

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})





from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

# relationship_app/views.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')'''