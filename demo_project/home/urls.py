
from django.urls import path
from home import views

urlpatterns = [
    # path('test/', views.test),
    # path('page/', views.page),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('ourmerch/', views.ourmerch),
]