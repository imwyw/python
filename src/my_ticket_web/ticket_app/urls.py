from django.urls import path
from . import views

urlpatterns = [
    path('left_ticket_list/', views.left_ticket_list, name='left_ticket_list'),
]
