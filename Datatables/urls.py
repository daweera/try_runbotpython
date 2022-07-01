from django.contrib import admin
from django.urls import path
from App import views  # ModuleNotFoundError: No module named 'App'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home")
]
