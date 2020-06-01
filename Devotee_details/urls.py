from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.add_devotee_details, name='add_devotee_details'),
]
