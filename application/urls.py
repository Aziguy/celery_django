from django.urls import path
from . import views

urlpatterns = [
    path("", views.make_some_iteration_view, name='iterate'),
]