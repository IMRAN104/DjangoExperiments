from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('admin/', admin.site.urls),
    path('message/', views.Message.as_view(), name='message')
]
