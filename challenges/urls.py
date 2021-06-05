from challenges.views import index
from django.urls import path
from . import views

urlpatterns = [
    path("january", views.index)
]