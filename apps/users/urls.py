from django.urls import path
from .views import register_user, index
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Login y logout
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_user, name="register"),

    path('user/', index, name="index"),


]
