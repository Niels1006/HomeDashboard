from django.urls import path

from api.views import DataAPI

urlpatterns = [
    path('data', DataAPI.as_view(), name='data'),
]
