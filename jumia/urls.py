from django.urls import path
from .views import home, myView

urlpatterns = [
    path("", home),
    path("home/", myView.as_view()),
]
