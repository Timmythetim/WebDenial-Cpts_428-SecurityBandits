from django.urls import path
from django.views.generic.base import TemplateView
from .views import PostDetailView
from . import views

urlpatterns = [
    path('', views.message_board, name = 'home'),
    path("register", views.register_request, name="register"),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("create", TemplateView.as_view(template_name='create.html'), name='create'),
    path('details/<int:pk>', PostDetailView.as_view(), name='details')
]