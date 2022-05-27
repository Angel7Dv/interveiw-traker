from django.urls import path
from .views import dashboard, vacant, view_enterprise
urlpatterns = [
    path('', dashboard, name="dashboard"), 
    path('<str:slug_enterprise>/<str:vacant_slug>/', vacant, name="vacant"), #allow delete
    path('<str:slug_enterprise>/', view_enterprise, name="view_enterprise"),

    # path('<str:enterprise>/<str:vacant>/<str:interview>', dashboard, name="dashboard"),

    
]
