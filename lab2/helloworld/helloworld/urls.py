from django.contrib import admin
from django.urls import path, include
from flatpages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.home, name='hello'),
    path('admin/', admin.site.urls),
]