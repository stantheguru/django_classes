from django.urls import path
from classes.views import AsyncView, MyFormView, SuccessView
from . import views



urlpatterns = [
    path("about", AsyncView.as_view()),
    path("name", MyFormView.as_view()),
    path("success", SuccessView.as_view())
]