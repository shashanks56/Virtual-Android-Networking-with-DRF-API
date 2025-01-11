
from django.urls import path
from .views import add_app, get_app, delete_app

urlpatterns = [
    path('add_app/', add_app),
    path('get_app/<int:id>/', get_app),
    path('delete_app/<int:id>/', delete_app),
]