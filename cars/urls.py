from django.urls import path
from .views import HomeView, NewCarView, CarDetailView, CarUpdateView, CarDeleteView


urlpatterns=[
     path("", HomeView.as_view(), name="home"),
     path("new_car/", NewCarView.as_view(), name="new_car"),   
     path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
     path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car_update"),
     path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
     #path("", home, name="home"),
     #path("new_car/", new_car_view, name="new_car"),  

]