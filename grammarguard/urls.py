from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("/analysis_results", views.analysis_results, name="analysis_results"),
]
