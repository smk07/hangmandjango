from django.urls import path
from . import views
urlpatterns = [
    path('', views.playagain),
    path('play',views.play),
    path('entry',views.entry),
    path('hang',views.hang)
]