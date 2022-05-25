from django.urls import path
from .views import register_user, user_panel
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register_user, name="register"),
    path('', user_panel, name="user_panel"),

    # Login y logout
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

]
