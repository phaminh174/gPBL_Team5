from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ListCreatePersonView.as_view()),
    path('person/', views.ListCreatePersonView.as_view()),
    path('person/<int:pk>', views.UpdateDeletePersonView.as_view()),
]
