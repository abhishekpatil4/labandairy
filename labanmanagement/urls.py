from django.urls import path
from labanmanagement import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('laagAccounts', views.laagAccounts, name='laagAccounts'),
    path('extras', views.extras, name='extras'),
    path('login', views.handlelogin, name='login'),
    path('logout', views.handlelogout, name='logout'),
    path('laagAccounts/<str:slug>', views.handleLaagAccounts, name='handleLaagAccounts'),
    path("cows", views.cows, name="cows"),
    path("cows/<str:slug>", views.handlecows, name="handlecows"),
    path('cows/<str:slug>/milk', views.milkrecord, name='milk'),
    path('cows/<str:slug>/medication', views.medication, name='medication'),
]
