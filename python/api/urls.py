from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hello/', views.hello),

    # path('get', views.get),
    # path('post', views.post),
]
