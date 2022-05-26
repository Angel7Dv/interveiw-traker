from django.urls import path
from .views import dashboard, delete_vacant, add_new_enterprise, view_enterprise
urlpatterns = [
    path('', dashboard, name="dashboard"),

    path('<str:name_enterprise>/', view_enterprise, name="view_enterprise"),

    # methods api
    path('delete-vacant/<int:vacant_id>/', delete_vacant, name="delete_vacant"),
    path('add-new-enterprise/<int:vacant_id>/', add_new_enterprise, name="add_new_enterprise"),

    # path('<str:enterprise>/<str:vacant>/<str:interview>', dashboard, name="dashboard"),

    
]
