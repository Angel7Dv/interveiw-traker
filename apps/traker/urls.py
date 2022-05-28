from django.urls import path
from .views import dashboard, vacant, enterprise, interview, add_interview
urlpatterns = [
    path('', dashboard, name="dashboard"), 


    path(r'<str:slug_enterprise>/', enterprise, name="enterprise"),
    
    path(r'add_interview/<str:vacant_slug>/', add_interview, name="add_interview"),

    path(r'<str:slug_enterprise>/<str:vacant_slug>/', vacant, name="vacant"), #allow delete
    path(r'<str:slug_enterprise>/<str:vacant_slug>/<str:interview_slug>/', interview, name="interview"), #allow delete


    # path('<str:enterprise>/<str:vacant>/<str:interview>', dashboard, name="dashboard"),

    
]