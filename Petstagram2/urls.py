
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Petstagram2.common.urls')),
    path('pets/',include('Petstagram2.pets.urls'))
]
