from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/details/', views.detail, name='detail'),
    path('<str:pk>/new-card/', views.newCard, name='new-card'),
    path('<str:list_id>/create-card/', views.create_card, name='create-card')
]