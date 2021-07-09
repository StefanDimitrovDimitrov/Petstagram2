from django.contrib import admin

# Register your models here.
from Petstagram2.accounts.models import UserProfile

admin.site.register(UserProfile)