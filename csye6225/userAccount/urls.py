from django.urls import path, include
from .views import UserAccountList

urlpatterns = [
    # Other URL patterns
    path('user/', UserAccountList.as_view(), name='UserAccountList'),
]
