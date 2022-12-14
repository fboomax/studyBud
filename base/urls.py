from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('room/create-room', views.createRoom, name= "create-room"),
    path('room/update-room/<str:pk>/', views.updateRoom, name= "update-room"),
    path('room/delete-room/<str:pk>/', views.deleteRoom, name= "delete-room"),
]