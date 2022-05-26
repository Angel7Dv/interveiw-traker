from django.urls import path
from .views import register_user, user_panel, index
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name="index"),

    path('user/', user_panel, name="user_panel"),
    path('register/', register_user, name="register"),

    # Login y logout
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

]
