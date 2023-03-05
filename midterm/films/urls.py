from django.urls import path
from films import views

urlpatterns = [
    path('api/films', views.film1),
    path('api/films/<int:pk>', views.film2)
]