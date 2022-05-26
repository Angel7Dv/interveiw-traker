from django.urls import path
from .views import dashboard, delete_vacant
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('delete-vacant/<int:vacant_id>/', delete_vacant, name="delete_vacant"),
    


    # path('<str:enterprise>', dashboard, name="dashboard"),
    # path('<str:enterprise>/<str:vacant>', dashboard, name="dashboard"),
    # path('<str:enterprise>/<str:vacant>/<str:interview>', dashboard, name="dashboard"),

    
]
