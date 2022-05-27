from django.urls import path
from .views import dashboard, vacant, view_enterprise, interview
urlpatterns = [
    path('', dashboard, name="dashboard"), 

    path(r'<str:slug_enterprise>/', view_enterprise, name="view_enterprise"),
    path(r'interview/<str:interview_slug>/', interview, name="interview"), #allow delete
    path(r'<str:slug_enterprise>/<str:vacant_slug>/', vacant, name="vacant"), #allow delete


    # path('<str:enterprise>/<str:vacant>/<str:interview>', dashboard, name="dashboard"),

    
]
