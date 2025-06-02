from django.urls import path
from .views import hello, index_view

urlpatterns = [
    path('hello/', hello),
    path("", index_view),
]