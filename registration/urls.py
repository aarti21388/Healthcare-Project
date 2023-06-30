from django.contrib import admin
from django.urls import include, path
from registration.views import registration_view
urlpatterns = [
    path('', registration_view, name="register"),
]
