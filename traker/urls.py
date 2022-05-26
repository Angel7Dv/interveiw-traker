from django.urls import path
from .views import dashboard, vacant, add_new_enterprise, view_enterprise
urlpatterns = [
    path('', dashboard, name="dashboard"), 

    path('<str:slug_enterprise>/', view_enterprise, name="view_enterprise"),

    # methods api
    path('vacant/<str:vacant_slug>/', vacant, name="vacant"), #allow delete

    path('add-new-enterprise/<int:vacant_id>/', add_new_enterprise, name="add_new_enterprise"),

    # path('<str:enterprise>/<str:vacant>/<str:interview>', dashboard, name="dashboard"),

    
]
