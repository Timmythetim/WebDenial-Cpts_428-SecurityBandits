from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, redirect
from django.core.exceptions import ValidationError
from .forms import NewUserForm, LoginForm, EditUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from .models import Profile, Post
from django.views.generic import DetailView, CreateView

def index(request):
    return HttpResponse("Hello, world.")

def logout_view(request):
    logout(request)
    return redirect("http://localhost:8000/login")

def message_board(request):
    posts = Post.objects.filter(published=True).order_by('-publish_date')
    return render(request, "home.html", {'posts' : posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'

def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password = password)
            print(user)
            if user:
                login(request, user)
                return redirect("http://localhost:8000/")
        else:
            return redirect("http://localhost:8000/login")
    login_form = LoginForm()
    return render(request, "registration/login.html", context={"login_form":login_form})

def edit_account(request):
    if request.method == 'POST':
        form = EditUserForm(request.user, request.POST)
        if form.is_valid():
            try:
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('http://localhost:8000/')
            except ValidationError as e:
                if e.code == 'invalid_username':
                    messages.error(request, 'The username  is already taken')
                else:
                    raise e
        else:
            messages.error(request, 'Please correct the error below.')
    form = EditUserForm(request.user)
    return render(request, template_name='registration/edit.html', context={'edit_form': form})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=True
            user.is_staff=False  
            user.is_admin=False
            user.is_superuser=False
            user.save()
            # user = authenticate(username=request.POST['username'], password = request.POST['password1'])
            # print("Password check passes?")
            # print(user.check_password(request.POST['password1']))
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("http://localhost:8000/login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})