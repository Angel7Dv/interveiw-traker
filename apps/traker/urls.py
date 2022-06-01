from django.urls import path
from .views import dashboard, vacant, enterprise, interview, post_interview, networking , post_networking
urlpatterns = [
    path('', dashboard, name="dashboard"), 

    path(r'<str:vacant_slug>/', vacant, name="vacant"), #allow delete

    path(r'<str:slug_enterprise>/', enterprise, name="enterprise"),
    path(r'<str:slug_enterprise>/networking/<int:pk>/', networking, name="networking"),
    
    path(r'post_interview/<str:vacant_slug>/', post_interview, name="post_interview"),
    path(r'post_networking/<str:vacant_slug>/', post_networking, name="post_networking"),
    # path(r'add_networking/<str:slug_enterprise>/', add_networking, name="add_networking"),

    path(r'<str:vacant_slug>/<int:pk>/', interview, name="interview"), #allow delete


    # path('<str:enterprise>/<str:vacant>/<str:interview>', dashboard, name="dashboard"),

    
]
