from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.main),
    path('', views.main1),
    path('remont/', views.remont),
    path('paint/', views.paint),
    path('tunning/', views.tunning),
    path('price/', views.price),
    path('comment/', views.comment),
    path('navbar/', views.navbar),
    path('company/', views.company),
    path('slide/', views.slide)
]
