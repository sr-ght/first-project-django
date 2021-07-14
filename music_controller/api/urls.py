# Define a visualição da página
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('', RoomView.as_view()),
]