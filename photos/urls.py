from django.urls import path
from .import views

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('photo/<str:pk>', views.viewPhoto, name = 'photo'),
    path('add/', views.addPhoto, name = 'add'),
    path('aboutUs/', views.aboutUs, name = 'aboutUs'),
    path('feedback/', views.feedback, name = 'feedback'),
    path('feedbacksub/', views.feedbacksub, name = 'feedbacksub'),
    path('sign/', views.sign, name = 'sign'),
    path('signsub/', views.signsub, name = 'signsub'),
    path('register/', views.register, name = 'register'),
    path('registersub/', views.registersub, name = 'registersub'),
    path('log/', views.logout_view, name = 'logout'),
]