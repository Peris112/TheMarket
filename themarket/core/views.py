from django.shortcuts import render, redirect

from items.models import Category, Items

from .forms import SignupForm

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def index(request):
    items = Items.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'items': items, 'categories': categories})

def home(request):
    return render(request, 'core/home.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')


def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')


def login_user(request):  # Renamed function for clarity, as 'login' is used internally by Django
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # The built-in login function must be called to establish the session
            login(request, user)
            messages.success(request, "You are now logged in!")

            # Admin redirection (redirect to a named URL, not hardcoded path)
            if user.is_superuser:
                # Assuming you have a URL pattern named 'admin_dashboard'
                return redirect('admin_dashboard')

                # For Normal Users redirection (redirect to a named URL)
            # Assuming you have a URL pattern named 'home_page'
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
            # For security, render the form again or redirect back to login
            return render(request, 'core/login.html')

    # This handles the initial GET request
    return render(request, 'core/login.html')


def signup_user(request):
    """Handles user registration (signup)."""
    if request.method == 'POST':
        # If you are using a custom form, replace UserCreationForm with it.
        # Ensure your custom form matches the fields rendered in signup.html: username, email, password1, password2.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after successful registration
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('core:home')  # Redirect to a home/dashboard page
        else:
            # Re-render the form with errors
            pass
    else:
        # Initialize the form for GET request
        form = UserCreationForm()

    # Context must pass the 'form' variable
    return render(request, 'core/signup.html', {'form': form})