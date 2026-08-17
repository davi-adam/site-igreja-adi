from django.contrib import admin
from django.urls import path
from institucional.views import home_teste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_teste),
]