from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("api/v1/", include("blog.api_urls")),
]