from django.urls import path
from . import views

urlpatterns = [
    path('show_list/', views.show_news_list, name='show_list'),
    path('save_action/', views.save_action, name='save_action'),
    path('edit_view/<int:id>/<str:title>', views.edit_view, name='edit_view'),
    path('ajax_view/', views.ajax_view, name='ajax_view'),
    path('ajax_data/', views.ajax_data, name='ajax_data'),
]
