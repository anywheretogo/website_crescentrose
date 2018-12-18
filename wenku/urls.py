from django.urls import path
from . import views

app_name = 'wenku'
urlpatterns = [
    path('', views.index ),
    path('index/', views.index, name='index'  )
    ]