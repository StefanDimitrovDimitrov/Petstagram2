from django.urls import path

from Petstagram2.common.views import landing_page

urlpatterns = [
    path('', landing_page)
]