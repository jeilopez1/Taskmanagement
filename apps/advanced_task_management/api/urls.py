from django.urls import path
from rest_framework import routers


from .views import CustomTokenObtainPairView,AddTaskView

routers = routers.SimpleRouter()
urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('rickandmorty/', AddTaskView.as_view(), name='rick_and_morty'),

]